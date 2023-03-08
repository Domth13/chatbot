import React, { useState, useEffect } from "react";
import "../../App.css";

const ChatbotResponse = ({ text, onComplete }) => {
  const [displayedText, setDisplayedText] = useState("");
  const [wordIndex, setWordIndex] = useState(0);

  useEffect(() => {
    const words = text ? text.split(" ") : [];
    const interval = setInterval(() => {
      if (wordIndex < words.length) {
        setDisplayedText((prev) => prev + " " + words[wordIndex]);
        setWordIndex((prev) => prev + 1);
      }
    }, 200);

    return () => clearInterval(interval);
  }, [text, wordIndex]);

  useEffect(() => {
    if (wordIndex >= text ? text.split(" ").length : []) {
      onComplete();
    }
  }, [wordIndex, text, onComplete]);

  return <span>{displayedText}</span>;
};

export default ChatbotResponse;
