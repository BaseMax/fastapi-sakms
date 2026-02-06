from fastapi import FastAPI
from .database import Base, engine
from .routers import auth, keys

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure API Key Management")

app.include_router(auth.router)
app.include_router(keys.router)


@app.get("/health")
def health():
    return {"status": "ok"}
