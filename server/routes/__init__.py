from typing import TYPE_CHECKING
from . import index

if TYPE_CHECKING:
    from fastapi import FastAPI


def load_routes(app: 'FastAPI'):
    app.include_router(index.router)
