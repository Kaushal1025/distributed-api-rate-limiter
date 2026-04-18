# Distributed API Rate Limiter

A Redis-backed distributed API rate limiting system built with FastAPI and Python to simulate backend traffic protection and abuse prevention similar to production systems used by large-scale platforms like Cloudflare.

## Features

- FastAPI backend with protected API endpoints
- Redis-based request tracking and caching
- Sliding window rate limiting logic
- Automatic HTTP 429 blocking for over-limit requests
- Per-client request quota enforcement
- Local testing with real browser/API requests

## Tech Stack

- Python
- FastAPI
- Redis
- Uvicorn
- VS Code
- Homebrew (Redis setup)

## How It Works

Each client request is tracked using Redis.

If a client exceeds the allowed request threshold within the configured time window:

- request is blocked
- HTTP 429 response is returned
- abuse prevention is enforced

This simulates real-world API protection systems used for traffic management and service reliability.

## Example Response

Successful request:

```json
{
  "message": "Request successful",
  "client_ip": "127.0.0.1",
  "remaining_requests": 4
}