from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.limiter import check_rate_limit

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Rate limiter is running"}

@app.get("/api/data")
def get_data(request: Request):
    client_ip = request.client.host

    allowed, remaining = check_rate_limit(client_ip)

    if not allowed:
        return JSONResponse(
            status_code=429,
            content={"error": "Rate limit exceeded"}
        )

    return {
        "message": "Request successful",
        "client_ip": client_ip,
        "remaining_requests": remaining
    }