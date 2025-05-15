from api.core.app import create_app
from api.core.database import init_db
from api.core.dependencies import init_dependencies
from api.core.exceptions import setup_exception_handlers

app = create_app()

init_db()

init_dependencies(app)

setup_exception_handlers(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)