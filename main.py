from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Minimal User API")


# Модели Pydantic для строгой типизации ответа
class Support(BaseModel):
    url: str
    text: str


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserResponse(BaseModel):
    data: UserData
    support: Support


# Фиктивная база данных пользователей (можно расширить)
users_db = {
    1: {
        "id": 1,
        "email": "george.bluth@reqres.in",
        "first_name": "George",
        "last_name": "Bluth",
        "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    2: {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    # при необходимости добавьте других пользователей
}

# Статичный блок support (одинаков для всех ответов)
support_info = Support(
    url="https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
    text="Tired of writing endless social media content? Let Content Caddy generate it for you."
)


@app.get("/api/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """
    Возвращает данные пользователя по его ID.
    Если пользователь не найден – возвращает 404.
    """
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    user = users_db[user_id]
    return UserResponse(data=UserData(**user), support=support_info)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)