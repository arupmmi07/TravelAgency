from langchain_openai import ChatOpenAI
from llm.models.llm_models import LLMModels
from llm.models.constants import DEFAULT_LLM_NAME
from llm.models.model import Model

from pydantic_core import PydanticCustomError
from pydantic import (
    BaseModel,
    Field,
    model_validator
)
from typing import Optional, Any, Dict


class LLMManager(BaseModel):

    llm_name: str = Field(
        description="Name of the model",
        default=DEFAULT_LLM_NAME
    )

    models: Dict[str, Model] = Field(
        description="Collection of supported models by the llm manager",
        default=LLMModels().models
    )

    config: Optional[Dict[str, Any]] = Field(
        description="Configuration for the llm manager",
        default=None,
    )

    def __init__(__pydantic_self__, **data):
        config = data.pop("config", {})
        super().__init__(**config, **data)

    @model_validator(mode="after")
    def set_attributes_based_on_config(self) -> "LLMManager":
        """Set attributes based on the LLMManager configuration."""
        print(self.config)
        if self.config:
            for key, value in self.config.items():
                setattr(self, key, value)
        return self
    
    def add_model(self, llm_name, base_url, temperature) -> "LLMManager":
        for key in self.config.items():
            if llm_name == key:
                raise PydanticCustomError(
                    "may_not_add_model", "This model is already added in the system", {}
                )
            return self.models
        self.models[llm_name]=Model(
            name=llm_name,
            base_url=base_url,
            temperature=temperature
        )
        return self
    
    def connect(self):
        return ChatOpenAI(
            model=self.models[self.llm_name].name,
            base_url=self.models[self.llm_name].base_url,
            temperature=self.models[self.llm_name].temperature
        )

    def get_model(self, llm_name) -> "Model":
        return self.models[llm_name]