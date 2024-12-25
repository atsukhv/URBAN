from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

# Подключение шаблонов
templates = Jinja2Templates(directory="module_16/module_16_5/templates")

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Временная база данных
users = [
    User(id=1, username="UrbanUser", age=24),
    User(id=2, username="UrbanTest", age=22),
    User(id=3, username="Capybara", age=60),
]

# Маршрут для отображения списка пользователей
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# Маршрут для отображения конкретного пользователя
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    return templates.TemplateResponse("users.html", {"request": request, "user": user})
