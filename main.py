from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from sqlalchemy.ext.asyncio import async_session

from database import get_session, async_session_generator
from dto import Tutorial
from service import save_tutorial

app = FastAPI()







@app.post('/items',
          status_code=status.HTTP_201_CREATED)
async def create_an_item(tutorial: Tutorial):

    tutorial = await save_tutorial(Tutorial(name=tutorial.name))
    return  tutorial





