import uvicorn
from .controller import app  # Import the FastAPI app

if __name__ == "__main__":
    uvicorn.run("app.controller:app", host="127.0.0.1", port=8000, reload=True)
