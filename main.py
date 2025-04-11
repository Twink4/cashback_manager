import uvicorn

from fastapi import FastAPI

from backend.banks.routers import router as banks_routers
from backend.mccs.routers import router as mccs_routers
from backend.mccs.routers import router as cashback_category_routers

app = FastAPI(
    title="Cashback Manager"
)

app.include_router(banks_routers)
app.include_router(mccs_routers)
app.include_router(cashback_category_routers)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True
    )
