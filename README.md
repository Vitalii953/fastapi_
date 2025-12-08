# FastAPI Item Manager

A simple REST API for managing items with FastAPI.

## Setup
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## API Endpoints
- `GET /` - Welcome message
- `GET /items/` - List all items
- `POST /items/` - Add new item

## Frontend
Open `src/index.html` in browser after starting the API.