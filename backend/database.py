from datetime import datetime
import motor.motor_asyncio
from models import ConversationSchema

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
db = client['chatbotDb']
collection = db['conversations']


async def save_conversation( conversation: ConversationSchema):
    timestamp = datetime.now()
    conversation = { 
        "user_msg": conversation["user_msg"], 
        "bot_msg": conversation["bot_msg"]
        }
    print(conversation)
    await collection.insert_one(conversation)

async def fetch_conversations():
    documents = []
    cursor = collection.find({})
    async for document in cursor:
        documents.append(ConversationSchema(**document))
    return documents

async def delete_conversations():
    result = await collection.delete_many({})
    if result.deleted_count == 0:
        return ("No conversations in collection.")
    else:
        return (f"{result.deleted_count} conversations were deleted.")