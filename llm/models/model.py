from pydantic import (
    BaseModel,
    Field
)
from typing import Optional, Any

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

    def __init__(__pydantic_self__, **data):
        config = data.pop("config", {})
        super().__init__(**config, **data)