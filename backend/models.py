from pydantic import BaseModel, Field, EmailStr, json
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

json.ENCODERS_BY_TYPE[ObjectId]=str
json.ENCODERS_BY_TYPE[PyObjectId]=str

class ConversationSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_msg: str = Field(...)
    bot_msg: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoder = {ObjectId: str}
        schema_extra = {
            "example": {
                "user_msg": "Hello?",
                "bot_msg": "How can I help?"
            }
        }