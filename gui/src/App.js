// gui/src/App.js

import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [target, setTarget] = useState('');
  const [scanType, setScanType] = useState('network');
  const [results, setResults] = useState('');

  const handleScan = async () => {
    let url = '';
    if (scanType === 'network') {
      url = 'http://localhost:8001/scan';
    } else if (scanType === 'web') {
      url = 'http://localhost:8002/scan';
    }

    const response = await axios.post(url, { target_ip: target });
    setResults(response.data);
  };

  return (
    <div className="container">
      <h1>Security Scanner</h1>
      <input
        type="text"
        value={target}
        onChange={(e) => setTarget(e.target.value)}
        placeholder="Enter target"
      />
      <select value={scanType} onChange={(e) => setScanType(e.target.value)}>
        <option value="network">Network Scan</option>
        <option value="web">Web Scan</option>
      </select>
      <button onClick={handleScan}>Scan</button>
      {results && <pre>{JSON.stringify(results, null, 2)}</pre>}
    </div>
  );
}

export default App;
