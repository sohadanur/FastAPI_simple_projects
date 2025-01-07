from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# In-memory storage for users
users = []
class UserCreate(BaseModel):
    user_id: int
    username: str 
@app.post("/create_user/")
async def create_user(user_data: UserCreate):
    user_id = user_data.user_id
    username = user_data.username
    
    # Add the user to the users list
    users.append(user_data)
    
    return {
        "message": "we got data successfully",
        "user_id": user_id,
        "username": username,
    }   

@app.get("/user_data/", response_model=list[UserCreate])
async def get_users():
    return users
    #return user_data

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000) 
