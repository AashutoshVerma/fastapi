from enum import Enum
from typing import Union
from fastapi import Request, APIRouter, Form
from fastapi.params import Query
from fastapi.responses import HTMLResponse
from config.db import conn
from pydantic import BaseModel


note = APIRouter()
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")


@note.get("/",response_class=HTMLResponse)
async def get_note(request: Request):
    docs = conn.test.Notes.find({})
    newDoc = []
    for doc in docs :
        newDoc.append({
            "id" : doc["_id"],
            "title" : doc["title"],
            "desc"  : doc["desc"]
        })
    return templates.TemplateResponse("index.html",{"request" : request,"newDoc" : newDoc})

@note.post("/")
async  def post_note(request : Request):
    note =await request.form()
    conn.test.Notes.insert_one(dict(note))
    return {"Success" : True}

@note.get("/item/{items}")
def path_func(items):
    return items


@note.get("/query")
def query_func(name : str, rollno : int):
    name = {"name":name,"rollno" : rollno}
    return (name)


@note.get("/query")
def query_func_union(rollno : int, name : Union[str, None] = None):
    name = {"name":name,"rollno" : rollno}
    return (name)

class model (str,Enum):
    India = "India",
    Australia = "Australia",
    England = "England"

@note.get("/chooseCountry")
def chooseCountry(country :model):
    return country


class Student(BaseModel):
    name : str
    Class : str
    percentage : Union[int,float,None] = None


@note.post("/student")
def student(student : Student):
    return student

# Putting Validation in the input fields
@note.get("/validation")
def validation(name : str = Query(default = None, min_length=5,max_length=10), rollno : int = Query(default=None)):
    return {"name" : name, "Roll No" : rollno}


# uploading form data from the frontend
@note.post("/formData")
def formData(email :str = Form(), password : str = Form()):
    return ({"email": email, "Password": password})

#upload file
from fastapi import File
@note.post("/getFileLen")
def getFileLen(file :bytes =  File()):
    return {"file_lenght" : len(file)}

from fastapi import UploadFile
@note.post("/uploadFile")
def uploadFile(file : UploadFile):
    return {"file" : file.filename}


#exceptoin handling
from fastapi import  HTTPException
@note.post("/errorHandling")
def errorHandling(value : int ):
    if value!=2 :
        return HTTPException(status_code=401,detail="Wrong Value")
    return value

#middleware Handling is defined in main.py

#Background Tasks

from fastapi import  BackgroundTasks;
import time
def sendMessage(message):
    time.sleep(10)
    print(message)
@note.get("/background")
def background(message : str,background_tasks : BackgroundTasks):
    background_tasks.add_task(sendMessage,message)
    return "Message will be sent in 10 secs...."