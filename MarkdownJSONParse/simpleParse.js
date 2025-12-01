#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

function parseLine(line) {
  // Split by | and clean up
  const parts = line.split('|').map(p => p.trim()).filter(p => p);
  return parts;
}

function parseNumber(str) {
  if (!str || str === '—' || str === '-' || str === '—') return null;
  const cleaned = str.replace(/[$,%]/g, '').replace(/,/g, '');
  const num = parseFloat(cleaned);
  return isNaN(num) ? null : num;
}

function main() {
  const filename = process.argv[2] || 'No AI Companies.txt';
  const outputFile = process.argv[3] || filename.replace('.txt', '.json');
  
  console.log(`Reading ${filename}...`);
  const file = fs.readFileSync(filename, 'utf8');
  const lines = file.split('\n');
  
  const result = {
    table1: [],
    table2: [],
    table3: []
  };
  
  let currentTable = 'table1';
  let headers = [];
  let isHeader = false;
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    
    if (line.includes('## Table')) {
      const tableNum = line.match(/Table (\d+)/)?.[1];
      if (tableNum && result[`table${tableNum}`]) {
        currentTable = `table${tableNum}`;
      }
      continue;
    }
    
    if (!line.startsWith('|')) continue;
    
    const parts = parseLine(line);
    
    // Check if this is a header line
    if (parts.includes('Ticker') && parts.includes('Current Ratio')) {
      headers = parts;
      isHeader = true;
      continue;
    }
    
    // Skip separator lines
    if (parts.every(p => p.match(/^[-\s]+$/))) {
      isHeader = false;
      continue;
    }
    
    // Skip if we haven't found headers yet
    if (headers.length === 0) continue;
    
    // Parse data row
    if (parts.length >= 5 && parts[0] !== 'Ticker') {
      const row = {};
      headers.forEach((header, idx) => {
        const value = parts[idx] || '';
        
        switch(header) {
          case 'Ticker': row.ticker = value; break;
          case 'Country': row.country = value; break;
          case 'Exchange': row.exchange = value; break;
          case 'Industry': row.industry = value; break;
          case 'Market Cap': row.marketCap = value; break;
          case 'P/FCF': row.pFcf = parseNumber(value); break;
          case 'Shares %': row.sharesPercent = parseNumber(value); break;
          case 'EBIT/Interest': row.ebitInterest = parseNumber(value); break;
          case 'Gross Profit %': row.grossProfitPercent = parseNumber(value); break;
          case 'EPS': row.eps = parseNumber(value); break;
          case 'P/B': row.pb = parseNumber(value); break;
          case 'FCF Margin %': row.fcfMarginPercent = parseNumber(value); break;
          case 'FCF Yield %': row.fcfYieldPercent = parseNumber(value); break;
          case 'Free Cash Flow': row.freeCashFlow = value; break;
          case 'Debt/Equity': row.debtEquity = parseNumber(value); break;
          case 'Debt Ratio': row.debtRatio = parseNumber(value); break;
          case 'Net Profit %': row.netProfitPercent = parseNumber(value); break;
          case 'Revenue Growth %': row.revenueGrowthPercent = parseNumber(value); break;
          case 'Net Growth %': row.netGrowthPercent = parseNumber(value); break;
          case 'P/E': row.pe = parseNumber(value); break;
          case 'Return on Equity %': row.returnOnEquityPercent = parseNumber(value); break;
          case 'Current Ratio': row.currentRatio = parseNumber(value); break;
        }
      });
      
      if (row.ticker && row.ticker !== '') {
        result[currentTable].push(row);
      }
    }
  }
  
  console.log(`Found ${result.table1.length} rows in table1`);
  console.log(`Found ${result.table2.length} rows in table2`);
  console.log(`Found ${result.table3.length} rows in table3`);
  console.log(`Total: ${result.table1.length + result.table2.length + result.table3.length} rows`);
  
  fs.writeFileSync(outputFile, JSON.stringify(result, null, 2));
  console.log(`Saved to ${outputFile}`);
}

if (require.main === module) {
  main();
}
