from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return ["Zee", "Ali", "Ahmed"]

@app.post("/users")
def create_user(name: str):
    return {"user": name}
