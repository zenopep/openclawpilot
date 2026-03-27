import React, { useState } from "react";
import { sendMessageToGennaro } from "./api";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input) return;

    const userMessage = { role: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);

    const res = await sendMessageToGennaro(input);

    const botMessage = {
      role: "gennaro",
      text: res.response || "Errore",
    };

    setMessages((prev) => [...prev, botMessage]);
    setInput("");
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Gennaro AI</h1>

      <div style={{ marginBottom: 20 }}>
        {messages.map((m, i) => (
          <div key={i}>
            <b>{m.role}:</b> {m.text}
          </div>
        ))}
      </div>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Scrivi a Gennaro..."
      />

      <button onClick={sendMessage}>Invia</button>
    </div>
  );
}

export default App;