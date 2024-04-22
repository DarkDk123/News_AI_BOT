from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Alive"}


# Function to run the server using Uvicorn programmatically
def keepAlive():
    uvicorn.run(app, host="0.0.0.0", port=8080)


# Directly calling the run function if this script is executed
if __name__ == "__main__":
    keepAlive()
