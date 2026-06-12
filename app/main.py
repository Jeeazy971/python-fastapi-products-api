from fastapi import FastAPI

app = FastAPI()


@app.get('/health')
async def health():
    return {
        "status": "ok"
    }


@app.get('/learning-status')
async def learning_status():
    return {
        "module": "FastAPI",
        "block": 1,
        "status": "in_progress"
    }
