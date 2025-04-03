import uvicorn

from fastapi import FastAPI

from backend.banks.routes import router as banks_routes

app = FastAPI(
    title="Cashback Manager"
)

app.include_router(banks_routes)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True
    )
