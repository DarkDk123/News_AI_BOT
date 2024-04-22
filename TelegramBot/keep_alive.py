"""
## keep_alive.py

This file contains a `FastAPI` Application, it is used to utilize
`render's` free Web service to eventually run our bot's `"main.py"` file.
"""

from fastapi import FastAPI
import uvicorn
from threading import Thread

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Alive"}


# Function to run the server using Uvicorn programmatically
def run() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8080)


def keepAlive() -> None:
    thread = Thread(target=run)
    thread.start()


# Directly calling the run function if this script is executed
if __name__ == "__main__":
    keepAlive()
