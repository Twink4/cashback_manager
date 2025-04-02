import uvicorn

from fastapi import FastAPI

from backend.banks.router import router as banks_routers

app = FastAPI(
    title="Cashback Manager"
)

app.include_router(banks_routers)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True
    )
