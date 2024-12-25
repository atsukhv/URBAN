from fastapi import FastAPI

users = {
    "0": "Имя: Exemple, Возраст: 20"
}

app = FastAPI()


@app.get("/users")
async def users_list():
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    user_id = str(int(max(users)) + 1)
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    del users[user_id]
    return f"The user {user_id} is deleted"