import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState("");
  
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
    setResult(data);
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
          <h2>Analysis</h2>

          <pre>{result}</pre>
        </div>
      )}
      </div>
  );
}

export default App;