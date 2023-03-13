from fastapi import FastAPI, HTTPException
from gpt_index import GPTSimpleVectorIndex
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_conversations, save_conversation, delete_conversations

app = FastAPI()
vector_index = GPTSimpleVectorIndex.load_from_disk("./vectorIndex/vectorIndex_new.json")

origins = [
    "http://localhost:3000" ### react.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#### routes ####
@app.get("/")
async def read_root():
    return("API IS WORKING.")

@app.get("/answer/{query}")
async def answer_me(query: str):
    personality = "You are a University Tutor Bot named BiWi in educational science and answer student questions. You are a friendly person and try to give good explanations."
    conversation_history = await fetch_conversations()
    prompt = personality + '\n'.join([f"user: {c.user_msg} \nbot: {c.bot_msg}" for c in conversation_history[-2:]]) + '\nuser: ' + query + '\nbot: '

    response = vector_index.query(prompt, response_mode="compact")
    if response:
        print(response)
        await save_conversation(conversation={"user_msg": query, "bot_msg": response.response})
        return {"response": "conversation successfull"}
    else:
        raise HTTPException(status_code=500, detail="No response from OpenAi Server.")
    
@app.get("/conversations")
async def get_conversations():
    response = await fetch_conversations()
    if response:
        return response
    return {"No conversations in database"}

@app.delete("/conversations")
async def del_conversations():
    response = await delete_conversations()
    if response:
        return response
    return {"No conversations in database"}