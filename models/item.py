from pydantic import BaseModel

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
