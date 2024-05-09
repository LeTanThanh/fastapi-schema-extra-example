from fastapi import FastAPI
from fastapi import Path
from fastapi import Body

from typing import Annotated

from models.item import Item

app = FastAPI()

# Extra JSON Schema data in Pydantic models
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body()]
):
  response = {"id": id, "item": item}

  return response
"""

# Field additional arguments
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[Item, Body(embed = True)]
):
  response = {"id": id, "item": item}

  return response
"""

# Body with examples
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[
    Item,
    Body(
      embed = True,
      examples = [{
        "name": "Item",
        "description": "A very nice Item",
        "price": 100.0,
        "tax": 1.0
      }]
    )
  ]
):
  response = {"id": id, "item": item}

  return response
"""

# Body with multiple examples
"""
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[
    Item,
    Body(
      embed = True,
      examples = [{
        "name": "Foo",
        "description": "A very nice Item",
        "price": 100.0,
        "tax": 1.0
      }, {
        "name": "Foo",
        "price": 100.0
      }]
    )
  ]
):
  response = {"id": id, "item": item}

  return response
"""

# Using the openapi_examples Parameter
@app.put("/items/{id}")
async def update_item(
  id: Annotated[int, Path()],
  item: Annotated[
    Item,
    Body(
      openapi_examples = {
        "normal": {
          "summary": "A normal example",
          "description": "A **normal** item works correctly.",
          "value": {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 100.0,
            "tax": 1.0
          }
        },
        "converted": {
          "summary": "An example with converted data",
          "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
          "value": {
            "name": "Foo",
            "price": 100.0
          }
        },
        "invalid": {
          "summary": "Invalid data is rejected with an error",
          "value": {
            "name": "Foo",
            "price": "one hundred"
          }
        }
      }
    )
  ]
):
  response = {"id": id, "item": item}

  return response
