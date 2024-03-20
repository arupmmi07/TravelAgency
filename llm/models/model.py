from pydantic import (
    BaseModel,
    Field,
    model_validator
)
from typing import Optional, Any, Dict

class Model(BaseModel):
    
    name: str = Field(
        description="Name of the model"
    )

    base_url: Optional[str] = Field(
        description="Base hosted url of the model",
        default=None
    )

    temperature: Optional[float] = Field(
        description="Default temperature of the model",
        default=None,
        ge=0.0,
        le=1.0
    )

    config: Optional[Dict[str, Any]] = Field(
        description="Configuration for the agent",
        default=None,
    )

    def __init__(__pydantic_self__, **data):
        config = data.pop("config", {})
        super().__init__(**config, **data)

    @model_validator(mode="after")
    def set_attributes_based_on_config(self) -> "Model":
        """Set attributes based on the model configuration."""
        if self.config:
            for key, value in self.config.items():
                setattr(self, key, value)
        return self