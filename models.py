from pydantic import BaseModel

# Define User Model
class User(BaseModel):
    id: int
    name: str
    email: str

# Define User Create (Without ID)
class UserCreate(BaseModel):
    name: str
    email: str
