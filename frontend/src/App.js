import React from "react";
import "./styles/App.css";
import Chatbot from "./components/Chatbot";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Oqila - Generative AI Chatbot</h1>
      </header>
      <main>
        <Chatbot />
      </main>
    </div>
  );
}

export default App;
