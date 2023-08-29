import React, { useState } from 'react';

function ApplicationForm() {
  const [applicationData, setApplicationData] = useState({
    businessName: '',
    yearEstablished: 0,
    loanAmount: 0,
    selectedYear: 0,
    selectedMonth: 0,
    profitOrLossSummary: []
  });

  const [preAssessment, setPreAssessment] = useState('');

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setApplicationData({
      ...applicationData,
      [name]: value
    });
  };

  const fetchBalanceSheet = async () => {
    const response = await fetch('/balance_sheet/fetch', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        year: applicationData.selectedYear,
        month: applicationData.selectedMonth
      })
    });

    if (response.ok) {
      const balanceSheetData = await response.json();
      setApplicationData({
        ...applicationData,
        profitOrLossSummary: [balanceSheetData, ...applicationData.profitOrLossSummary]
      });
    }
  };

  const submitApplication = async () => {
    const response = await fetch('/application/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(applicationData)
    });

    if (response.ok) {
      const decisionEngineResult = await response.json();
      setPreAssessment(decisionEngineResult.preAssessment);
    }
  };
  return (
    <div>
    <div>
    <label>Business Name:</label>
    <input
      type="text"
      name="businessName"
      value={applicationData.businessName}
      onChange={handleInputChange}
    />
  </div>
  <div>
    <label>Year Established:</label>
    <input
      type="number"
      name="yearEstablished"
      value={applicationData.yearEstablished}
      onChange={handleInputChange}
    />
  </div>
  <div>
    <label>Loan Amount:</label>
    <input
      type="number"
      name="loanAmount"
      value={applicationData.loanAmount}
      onChange={handleInputChange}
    />
  </div>
  <div>
    <label>Year:</label>
    <input
      type="number"
      name="selectedYear"
      value={applicationData.selectedYear}
      onChange={handleInputChange}
    />
  </div>
  <div>
    <label>Month:</label>
    <input
      type="number"
      name="selectedMonth"
      value={applicationData.selectedMonth}
      onChange={handleInputChange}
    />
  </div>
  <button onClick={fetchBalanceSheet}>Fetch Balance Sheet</button>
  <h2>Profit or Loss Summary</h2>
  <ul>
    {applicationData.profitOrLossSummary.map((entry, index) => (
      <li key={index}>
        Year: {entry.year}, Month: {entry.month}, Profit/Loss: {entry.profitOrLoss}, Assets Value: {entry.assetsValue}
      </li>
    ))}
  </ul>
  <button onClick={submitApplication}>Submit Application</button>
  {preAssessment && <p>Pre-assessment: {preAssessment}</p>}
  </div>
  );
}

export default ApplicationForm;
