import React from "react";

const App: React.FC = () => {
  return (
    <div
      style={{
        padding: "20px",
        fontFamily: "sans-serif",
        color: "#fff",
        background: "#222",
      }}
    >
      <h1>Memora AI</h1>
      <p>Highlighted Text Will Appear Here</p>
      <input
        type="text"
        placeholder="Ask a question..."
        style={{ width: "95%", padding: "10px" }}
      />
      <div
        style={{
          marginTop: "20px",
          borderTop: "1px solid #444",
          paddingTop: "20px",
        }}
      >
        <h2>Conversation History</h2>
        <p>AI responses will show up here...</p>
      </div>
    </div>
  );
};

export default App;
