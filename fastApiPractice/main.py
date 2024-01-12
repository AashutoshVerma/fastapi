from fastapi import FastAPI, Request
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from routes.notes import  note
app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")

# Api versioning
app.include_router(note, prefix="/v1")


#midddleware handling

# @app.middleware("http")
# async  def middlewareHandling(request : Request, call_next):
#     print("Before requesting")
#     # if "value" not in request.query_params:
#     #     raise HTTPException(status_code=401,detail="Invalid path Parameter")
#     response = await  call_next(request)
#     print("After Requesting")
#     return response
#
# @app.get("/")
# def home():
#     return {"hello"}
