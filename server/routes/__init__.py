from typing import TYPE_CHECKING
from . import index, delete

if TYPE_CHECKING:
    from fastapi import FastAPI


def load_routes(app: 'FastAPI'):
    app.include_router(index.router)
    app.include_router(delete.router)
