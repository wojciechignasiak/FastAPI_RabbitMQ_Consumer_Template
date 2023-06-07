from fastapi import FastAPI


def create_application() -> FastAPI:
    application = FastAPI(openapi_url="/example/openapi.json", docs_url="/example/docs")


    return application

app = create_application()


@app.on_event("startup")
async def startup_event():
    print("Starting example-service...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting example-service down...")