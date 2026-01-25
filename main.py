from fastapi import FastAPI

app = FastAPI(title="My First FastAPI Project")

users = [
    {"id": 1, "name": "zikrullah"},
    {"id": 2, "name": "Zee"}
]

@app.get("/")
def root():
    return {"message": "Welcome to my first FastAPI project"}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}
