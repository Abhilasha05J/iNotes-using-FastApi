from http.client import HTTPException

from bson import ObjectId
from fastapi import APIRouter
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from bson import ObjectId
from schemas.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    print("Handling request to '/'")
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs :
        print(doc)
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc.get("title", "No Title"),
            "desc": doc.get("desc", "No desc"),
            "imp":doc.get("imp", "No imp"),
        })
        print(newDocs)
    return templates.TemplateResponse("index.html",{"request":request, "newDocs":newDocs})

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["imp"] = True if formDict.get("imp") == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"message":"Saved Successfully"}

# @note.delete("/{id}")
# async def delete_item(id:str):
#     try:
#         object_id = ObjectId(id)
#     except Exception:
#         raise HTTPException(status_code=400, detail="Invalid ID Format")
#
#     delete_result = conn.notes.notes.delete_one({"_id":ObjectId(id)})
#     if delete_result.deleted_count == 1:
#         return{"message":"Deleted Successfully"}
#
#     raise HTTPException(status_code=404, detail="Not Found")

