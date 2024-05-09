from pydantic import BaseModel
from pydantic import Field

# Extra JSON Schema data in Pydantic models
"""
class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None

  model_config = {
    "json_schema_extra": {
      "examples": [{
        "name": "Item",
        "description": "A very nice Item",
        "price": 100.0,
        "tax": 1.0
      }]
    }
  }
"""

# Field additional arguments
"""
class Item(BaseModel):
  name: str = Field(examples = ["Item"])
  description: str | None = Field(default =None, examples = ["A very nice Item"])
  price: float = Field(examples = [100.0])
  tax: float | None = Field(default = None, examples = [1.0])
"""

# Body with examples¶
class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None
