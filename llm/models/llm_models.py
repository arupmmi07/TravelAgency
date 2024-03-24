import os
from llm.models.constants import *
from llm.models.model import Model

from dotenv import load_dotenv
load_dotenv()

class LLMModels:
    def __init__(self):
        self.models = {
            DEFAULT_GPT4: Model(
                name=DEFAULT_GPT4, 
                base_url=os.environ['OPENAI_API_BASE'], 
                temperature=DEFAULT_TEMPERATURE
            ),
            DEFAULT_GPT35: Model(
                name=DEFAULT_GPT35, 
                base_url=os.environ['OPENAI_API_BASE'], 
                temperature=DEFAULT_TEMPERATURE
            ),
            DEFAULT_LLAMA2: Model(
                name=DEFAULT_LLAMA2, 
                base_url=os.environ['OLLAMA_API_BASE'], 
                temperature=DEFAULT_TEMPERATURE
            ),
            DEFAULT_MISTRAL: Model(
                name=DEFAULT_MISTRAL, 
                base_url=os.environ['OLLAMA_API_BASE'], 
                temperature=DEFAULT_TEMPERATURE
            )
        }