import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  
  const analyzeMessage = async () => {
    const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            message: message
        }),
    });

    const data = await response.json();
    setResult(data.analysis);
  };

  return (
    <div className="container">
      <h1>🛡️ ScamGuardian AI</h1>

      <p>Paste a suspicious SMS below.</p>

      <textarea
        rows="8"
        placeholder="Paste SMS here..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={analyzeMessage}>
        Analyze Message
      </button> 
      {result && (
        <div className="result">
          <h2>🛡 Scam Analysis</h2>

          <h3>{result.level} RISK ({result.risk}%)</h3>

          <p><strong>Type:</strong> {result.type}</p>

          <p><strong>Summary:</strong></p>
          <p>{result.summary}</p>

          <h4>🚩 Warning Signs</h4>
          <ul>
            {result.flags.map((flag, index) => (
              <li key={index}>{flag}</li>
            ))}
          </ul>

          <h4>✅ What You Should Do</h4>
          <ul>
            {result.advice.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;