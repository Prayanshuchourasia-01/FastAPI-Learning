from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message":"my First API is working"}

