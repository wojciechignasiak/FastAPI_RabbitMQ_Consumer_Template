from fastapi import FastAPI
import asyncio
from app.rabbitmq.consumer.startup_consumer import rabbitmq_consumer
from app.routers import (
    tik
)

def create_application() -> FastAPI:
    application = FastAPI(openapi_url="/fastapi-rabbitmq/openapi.json", docs_url="/fastapi-rabbitmq/docs")
    application.include_router(tik.router, prefix="/fastapi-rabbitmq", tags=["fastapi-rabbitmq"])
    return application

app = create_application()


@app.on_event("startup")
async def startup_event():
    print("Starting fastapi-rabbitmq app...")
    loop = asyncio.get_event_loop()
    rabbitmq_task = loop.create_task(rabbitmq_consumer(loop))

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting fastapi-rabbitmq app down...")