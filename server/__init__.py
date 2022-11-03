from server.elastic import connect_elasticsearch, get_elastic
from server.database import init_database
from fastapi import FastAPI
import server.routes

app = FastAPI()
routes.load_routes(app)


@app.on_event("startup")
async def startup_event():
    await database.init_database()
    await connect_elasticsearch()


@app.on_event("shutdown")
async def shutdown_event():
    _elastic = get_elastic()
    await _elastic.close()
