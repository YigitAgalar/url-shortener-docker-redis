from fastapi import FastAPI,Request
from fastapi.responses import RedirectResponse,HTMLResponse
from .data_schema import Task
from .shortener import url_shorter
from fastapi.templating import Jinja2Templates
from .routers.login import router 
from prometheus_fastapi_instrumentator import Instrumentator



app = FastAPI()

Instrumentator().instrument(app).expose(app)

#templates = Jinja2Templates(".\\app\\views")


#templates=Jinja2Templates(".\\app\\views")



@app.get('/')
def root():
    return {"message":"alive"}


#@app.get("/users", response_class=HTMLResponse)
#async def user(request:Request):
   
#    return templates.TemplateResponse("index.html",{"request":request})



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



app.include_router(router)