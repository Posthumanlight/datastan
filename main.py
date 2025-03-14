from fastapi import FastAPI, Body
import uvicorn
from models.db_connection import get_db
from models.db_setup import create_table_questions_stable
app = FastAPI()

@app.get("/")
async def get_root(user):
    return f"Hello {user}"

@app.post("/")
async def post_root(user:str = Body(embed=True)):
    return f"Hello {user}. You posted this"

@app.get("/adm/tests")
async def test_connection():
    db = get_db()
    return "Connection successful"

if __name__ == "__main__":
    create_table_questions_stable()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)