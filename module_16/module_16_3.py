from fastapi import FastAPI, HTTPException

users = {
    "1": "Имя: Example, Возраст: 18"
}

app = FastAPI()


@app.get("/users")
async def users_list():
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    if age <= 0:
        raise HTTPException(status_code=400, detail="Возраст должен быть положительным числом")

    user_id = str(len(users) + 1)
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if age <= 0:
        raise HTTPException(status_code=400, detail="Возраст должен быть положительным числом")

    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    del users[user_id]
    return f"The user {user_id} is deleted"