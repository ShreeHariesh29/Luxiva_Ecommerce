from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from connector import connection


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] to allow only React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/home")
def home():
    conn = connection()
    cursor = conn.cursor()
    query = "select * from product_items"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

