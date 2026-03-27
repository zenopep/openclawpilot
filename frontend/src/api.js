const API_URL = process.env.REACT_APP_API_URL;

export async function sendMessageToGennaro(prompt) {
  const res = await fetch(`${API_URL}/api/agent/gennaro`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ prompt }),
  });

  return res.json();
}