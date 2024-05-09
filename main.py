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
# @app.put("/items/{id}")
# async def update_item(
#   id: Annotated[int, Path()],
#   item: Annotated[Item, Body(embed = True)]
# ):
#   response = {"id": id, "item": item}

#   return response
