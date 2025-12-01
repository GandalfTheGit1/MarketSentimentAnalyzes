#!/usr/bin/env node
/**
 * Utility script that parses one or more Markdown tables containing
 * fundamental data (like the "No AI Companies" sheet) and emits a JSON
 * payload that matches the schema already used inside
 * NonAICompanies.json.
 *
 * Usage:
 *   pnpm node markdownTablesToJson.js "No AI Companies.txt" NonAICompanies.json
 *   node markdownTablesToJson.js "No AI Companies.txt" > NonAICompanies.json
 */
const fs = require("fs");
const path = require("path");

const HEADER_TO_KEY = {
  "Ticker": "ticker",
  "Country": "country",
  "Exchange": "exchange",
  "Industry": "industry",
  "Market Cap": "marketCap",
  "P/FCF": "pFcf",
  "Shares %": "sharesPercent",
  "EBIT/Interest": "ebitInterest",
  "Gross Profit %": "grossProfitPercent",
  "EPS": "eps",
  "P/B": "pb",
  "FCF Margin %": "fcfMarginPercent",
  "FCF Yield %": "fcfYieldPercent",
  "Free Cash Flow": "freeCashFlow",
  "Debt/Equity": "debtEquity",
  "Debt Ratio": "debtRatio",
  "Net Profit %": "netProfitPercent",
  "Revenue Growth %": "revenueGrowthPercent",
  "Net Growth %": "netGrowthPercent",
  "P/E": "pe",
  "Return on Equity %": "returnOnEquityPercent",
  "Current Ratio": "currentRatio"
};

const RAW_STRING_FIELDS = new Set(["marketCap", "freeCashFlow"]);
const NUMERIC_FIELDS = new Set(
  Object.values(HEADER_TO_KEY).filter((key) => !RAW_STRING_FIELDS.has(key))
);

function isNullish(value) {
  if (value == null) return true;
  const trimmed = value.trim();
  return (
    trimmed === "" ||
    trimmed === "-" ||
    trimmed === "--" ||
    trimmed === "—" ||
    trimmed === "–" ||
    trimmed.toLowerCase() === "null"
  );
}

function parseNumber(raw) {
  if (isNullish(raw)) return null;
  const cleaned = raw
    .replace(/[$,%]/g, "")
    .replace(/\s+/g, "")
    .replace(/,/g, "");
  if (cleaned === "" || cleaned === "-" || cleaned === "--") return null;
  const value = parseFloat(cleaned);
  return Number.isNaN(value) ? null : value;
}

function mapRow(columns, values) {
  const row = {};
  columns.forEach((column, idx) => {
    const key = HEADER_TO_KEY[column];
    if (!key) return;
    const rawValue = values[idx]?.trim() ?? "";
    if (RAW_STRING_FIELDS.has(key)) {
      row[key] = isNullish(rawValue) ? null : rawValue;
    } else if (NUMERIC_FIELDS.has(key)) {
      row[key] = parseNumber(rawValue);
    } else {
      row[key] = isNullish(rawValue) ? null : rawValue;
    }
  });
  return row;
}

function normalizeTableName(label, fallbackIndex) {
  if (label) {
    const match = label.match(/table\s*(\d+)/i);
    if (match) {
      return `table${match[1]}`;
    }
  }
  return `table${fallbackIndex}`;
}

function parseMarkdownTables(markdown) {
  const lines = markdown.split(/\r?\n/);
  const tables = {};
  const tableTickers = {};
  let pendingHeading = null;
  let tableCount = 0;
  let processedLines = 0;

  console.log("Starting to parse lines...");

  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    processedLines++;
    
    // Progress indicator every 100 lines
    if (processedLines % 100 === 0) {
      console.log(`Processed ${processedLines}/${lines.length} lines...`);
    }

    const headingMatch = line.match(/^##\s+Table\s*(\d+)/i);
    if (headingMatch) {
      pendingHeading = headingMatch[0];
      console.log(`Found heading: ${pendingHeading}`);
      i++;
      continue;
    }

    // More flexible header detection - look for Ticker in any position
    if (!line.startsWith("|") || !line.includes("Ticker")) {
      i++;
      continue;
    }

    // Check if this looks like a header row (has common columns)
    const hasCommonColumns = line.includes("Market Cap") || line.includes("P/E") || line.includes("Current Ratio");
    if (!hasCommonColumns) {
      i++;
      continue;
    }

    // Header row detected
    tableCount += 1;
    const tableName = normalizeTableName(pendingHeading, tableCount);
    pendingHeading = null;
    console.log(`Starting table: ${tableName}`);

    if (!tables[tableName]) {
      tables[tableName] = [];
      tableTickers[tableName] = new Set();
    }

    const headerColumns = line
      .split("|")
      .slice(1, -1)
      .map((cell) => cell.trim());

    // Skip the separator line (---|---)
    i += 1;
    if (i < lines.length && lines[i].match(/^\s*\|[\s\-\|]+\s*\|?\s*$/)) {
      i += 1;
    }

    let rowsInTable = 0;
    // Collect data rows until we hit another header or end of file
    while (i < lines.length) {
      const dataLine = lines[i];
      if (!dataLine.startsWith("|")) {
        i++;
        break;
      }
      
      // Check if this is a new header row
      if (dataLine.includes("Ticker") && 
          (dataLine.includes("Market Cap") || dataLine.includes("P/E") || dataLine.includes("Current Ratio"))) {
        break; // Don't back up, let the outer loop handle it
      }

      const cells = dataLine
        .split("|")
        .slice(1, -1)
        .map((cell) => cell.trim());

      // Skip empty or malformed rows
      if (cells.length < 5 || cells[0] === "" || cells[0] === "Ticker") {
        i++;
        continue;
      }

      // Adjust for mismatched column counts
      const adjustedCells = cells.slice(0, headerColumns.length);
      while (adjustedCells.length < headerColumns.length) {
        adjustedCells.push("");
      }

      const row = mapRow(headerColumns, adjustedCells);
      if (!row.ticker) {
        i++;
        continue;
      }

      const mapKey = String(row.ticker);
      if (tableTickers[tableName].has(mapKey)) {
        i++;
        continue;
      }
      tableTickers[tableName].add(mapKey);
      tables[tableName].push(row);
      rowsInTable++;
      
      i++;
    }
    
    console.log(`Completed ${tableName}: ${rowsInTable} rows`);
  }

  console.log(`Finished processing ${processedLines} lines`);
  return tables;
}

function main() {
  const [, , inputPath, outputPath] = process.argv;
  if (!inputPath) {
    console.error("Usage: node markdownTablesToJson.js <markdownPath> [outputPath]");
    process.exit(1);
  }

  console.log(`Reading markdown file: ${inputPath}`);
  const absoluteInput = path.resolve(process.cwd(), inputPath);
  const content = fs.readFileSync(absoluteInput, "utf8");
  console.log(`File loaded, size: ${content.length} characters`);
  
  console.log("Parsing markdown tables...");
  const parsed = parseMarkdownTables(content);
  
  const tableNames = Object.keys(parsed);
  console.log(`Found ${tableNames.length} tables: ${tableNames.join(", ")}`);
  
  let totalRows = 0;
  tableNames.forEach(name => {
    const count = parsed[name].length;
    totalRows += count;
    console.log(`  ${name}: ${count} rows`);
  });
  console.log(`Total rows parsed: ${totalRows}`);
  
  const json = JSON.stringify(parsed, null, 2);
  console.log(`JSON output size: ${json.length} characters`);

  if (outputPath) {
    const absoluteOutput = path.resolve(process.cwd(), outputPath);
    fs.writeFileSync(absoluteOutput, json);
    console.log(`✅ Saved ${absoluteOutput}`);
  } else {
    process.stdout.write(json);
  }
}

if (require.main === module) {
  main();
}

module.exports = { parseMarkdownTables };
