from langchain_openai import ChatOpenAI
from llm.models.llm_models import LLMModels
from llm.models.constants import DEFAULT_MODEL
from llm.models.model import Model


class LLMManager:
    def __init__(self, model_name=DEFAULT_MODEL):
        self.llm_models=LLMModels()
        self.model=self.llm_models.models[model_name]
    
    def connect(self):
        return ChatOpenAI(
            model=self.model.name,
            base_url=self.model.base_url,
            temperature=self.model.temperature
        )
    
    def add_model(self, name, base_url, temperature):
        self.llm_models.models[name]=Model(
            name=name,
            base_url=base_url,
            temperature=temperature
        )
        self.model=self.llm_models.models[name]
        return self.model
    
    def get_model(self, name):
        return self.llm_models.models[name]