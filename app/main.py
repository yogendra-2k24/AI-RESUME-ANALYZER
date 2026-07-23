from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "AI Resume Analyzer API is running"}