from fastapi import FastAPI, HTTPException
from gpt_index import GPTSimpleVectorIndex
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_conversations, save_conversation, delete_conversations

app = FastAPI()
vector_index = GPTSimpleVectorIndex.load_from_disk("./vectorIndex/vectorIndex.json")

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
    response = vector_index.query(query, response_mode="compact")
    if response:
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