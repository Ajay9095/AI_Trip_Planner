import os
from dotenv import load_dotenv
from typing import Any, Optional, Literal
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain import llm




class ConfigLoader:
    def __init__(self):
        print(f"Loading configuration...")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]
    

class ModelLoader(BaseModel):
    model_provider: Literal["openai", "groq"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context:Any) -> None:
        self,config = ConfigLoader()

    
    class config:
        arbitrary_types_allowed = True
        

    def load_llm(self):
        '''
        Load the LLM based on the provider specified in the config.
        '''

        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading Groq model...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm.ChatGroq(
                model=model_name,
                api_key=groq_api_key
            )
        elif self.model_provider == "openai":
            print("Loading OpenAI model...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm.ChatOpenAI(
                model=model_name,
                api_key=openai_api_key
            )