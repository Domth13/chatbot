import React, { useState } from 'react';
import "../../App.css"
import ChatbotResponse from '../ChatbotResponse';

function Conversation({ conversation }) {
  const [showCursor, setShowCursor] = useState(true);

  const handleChatbotResponseComplete = () => {
    setShowCursor(false);
  }

  if (!conversation || !conversation.user_msg) {
    return <div className='Conversation-bot'>Hey, I am BiWiBot. How can I help you?</div>;
  }
  const lastBotMessageIndex = conversation ? conversation.bot_msg.length > 0 ? conversation.bot_msg.length - 1 : null : null;

  return (
    <div>
      {conversation.user_msg.map((msg, index) => (
        <div key={index}>
          <div className='Conversation-user'>{`User: ${msg}`}</div>
          <div className='Conversation-bot'>
            {"BiWiBot:"} {index === lastBotMessageIndex ?
              <ChatbotResponse text={conversation.bot_msg[index]} onComplete={handleChatbotResponseComplete} />
              :
              <span>{conversation.bot_msg[index]}</span>
            }
            {index === lastBotMessageIndex && showCursor && <div className="blink-cursor"></div>}
          </div>
        </div>
      ))}
    </div>
  );
}

export default Conversation;
