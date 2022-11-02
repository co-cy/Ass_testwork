from fastapi import FastAPI
import server.routes

app = FastAPI()

routes.load_routes(app)
