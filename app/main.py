from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel,  validator
from fastapi.responses import RedirectResponse
from .data_schema import Task
from .shortener import url_shorter
from urllib.parse import unquote
app = FastAPI()

@app.get('/')
def root():
    return {"message":"alive"}


@app.get("/{url_item}")
def go_to_link(url_item: str):
    for pks in list(Task.all_pks()):
        task=Task.get(pks)
        if task.url_str==url_item:
            
            task.click_count=task.click_count+1
            task.save()
            return RedirectResponse(task.original_url)


@app.post("/task/{url:path}")
async def kayit_olustur(url=str): 
    task =url_shorter(url)
    if task.expire_date==-99:
        return task.save()
    else:
        task.save()
        return task.expire(task.expire_date*86400)
