from langchain.utils.openai_functions import convert_pydantic_to_openai_tool
from pydantic import BaseModel,Field
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("Open_api_key")


class PersonInfo(BaseModel):
    """Get the information of a person"""
    name: str = Field(..., title="Name of the person")

model=ChatOpenAI(temperature=0)

open_ai_function=convert_pydantic_to_openai_tool(PersonInfo)

prompt=ChatPromptTemplate.from_messages(
    {
        ("system","check_person_info"),
        ("user","{input}")
    }
)
 



