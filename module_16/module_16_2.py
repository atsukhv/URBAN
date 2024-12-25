from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Главная страница"}


@app.get("/user/{user_id}")
async def read_user(user_id: Annotated[int, Path(gt=0,
                                                 le=100,
                                                 title="User ID",
                                                 description="Enter User ID",
                                                 example=1)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def read_user(username: Annotated[str, Path(min_length=5, max_length=20, title="User name",
                                                  description="Enter username", example="Albert Sukhanov")],
                    age: Annotated[int, Path(gt=18, le=120, title="User age",
                                             description="Enter age", example=21)]):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


