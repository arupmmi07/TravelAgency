from langchain_openai import ChatOpenAI
from llm.models.llm_models import LLMModels
from llm.models.constants import DEFAULT_MODEL


class LLMManager:
    def __init__(self, model_name=DEFAULT_MODEL):
        self.models=LLMModels()
        self.model=self.models.models[model_name]
    def connect(self):
        return ChatOpenAI(
            model=self.model.name(),
            base_url=self.model.base_url(),
            temperature=self.model.temperature()
        )