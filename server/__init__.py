from server.database import init_database
from fastapi import FastAPI
import server.routes

app = FastAPI()
routes.load_routes(app)


@app.on_event("startup")
async def startup_event():
    await database.init_database()
