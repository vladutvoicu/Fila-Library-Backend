from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.scheduler import scheduler

from app.api.endpoints.books import books_router
from app.api.endpoints.auth import auth_router
from app.api.endpoints.authors import authors_router
from app.api.endpoints.publishers import publishers_router
from app.api.endpoints.collections import collections_router
from app.api.endpoints.inventory import inventory_router
from app.api.endpoints.borrows import borrows_router
from app.api.endpoints.persons import persons_router
from app.api.endpoints.statistics import statistics_router

app = FastAPI()

origins = ["http://localhost:3000", "https://fila-library.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(authors_router, prefix="/api")
app.include_router(publishers_router, prefix="/api")
app.include_router(collections_router, prefix="/api")
app.include_router(inventory_router, prefix="/api")
app.include_router(borrows_router, prefix="/api")
app.include_router(persons_router, prefix="/api")
app.include_router(statistics_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    scheduler.start()

    uvicorn.run(app, host="0.0.0.0", port=8000)
