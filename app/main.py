from fastapi import FastAPI;

app = FastAPI()

@app.get('/')
def home():
    return {"message": "hey, i am fast api"}