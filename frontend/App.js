import React, { useState } from 'react';

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const sendToBackend = async () => {
    const res = await fetch('/api/speak', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ text: input })
    });
    const data = await res.json();
    setResponse(data.reply);
  }

  return (
    <div>
      <input onChange={e => setInput(e.target.value)} />
      <button onClick={sendToBackend}>Send</button>
      <p>{response}</p>
    </div>
  );
}

export default App;
