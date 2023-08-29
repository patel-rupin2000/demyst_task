import React from 'react';

function BalanceSheet({ summary }) {
  return (
    <div>
      <h2>Profit or Loss Summary</h2>
      <ul>
        {summary.map((entry, index) => (
          <li key={index}>
            Year: {entry.year}, Month: {entry.month}, Profit/Loss: {entry.profitOrLoss}, Assets Value: {entry.assetsValue}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BalanceSheet;
