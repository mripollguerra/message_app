from fastapi import FastAPI
from containers import Container

def init_dependencies(app: FastAPI):
    container = Container()
    container.wire(packages=["api.v1.company", "api.v1.message"])
    app.container = container
    return container