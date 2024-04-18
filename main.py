from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import socket

app = FastAPI()

@app.get("/factorial/{number_input}")
async def factorial(number_input: int):
    result = 1
    for i in range(1, number_input + 1):
        result *= i
    return {"number": number_input, "factorial": result}

@app.get("/whoami")
async def whoami():
    ip = socket.gethostbyname(socket.gethostname())
    time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
    return {"client": ip, "time": time}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
