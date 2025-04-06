import uvicorn

from fastapi import FastAPI

from backend.banks.routes import router as banks_routes
from backend.mccs.routes import router as mccs_routes

app = FastAPI(
    title="Cashback Manager"
)

app.include_router(banks_routes)
app.include_router(mccs_routes)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True
    )
