from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from config.Db import conn
from fastapi.templating import Jinja2Templates
from models.noteModel import Note as Item
note = APIRouter()
templates = Jinja2Templates(directory = "templates")

@note.get("/",response_class=HTMLResponse)
async def get_Note( request: Request) :
    docs = conn.test.Notes.find({})
    newDoc  = []
    for doc in docs :
        newDoc.append({
            "id" : doc["_id"],
            "title" : doc["title"],
            "desc" : doc["desc"]
        })
    return templates.TemplateResponse("index.html",{"request" : request , "newDoc" : newDoc})

@note.post("/")
async  def post_Note(request : Request):
    form = await request.form()
    note = conn.test.Notes.insert_one(dict(form))
    return {"Success" : True}
