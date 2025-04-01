from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Cashback Manager"
)

#app.include_router()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True
    )