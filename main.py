from fastapi import FastAPI
from controllers import userController

app = FastAPI()

# Include User API
app.include_router(userController.router)
