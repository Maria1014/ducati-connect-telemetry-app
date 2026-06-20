from fastapi import FastAPI

app = FastAPI(
    title="Ducati Connect Telemetry API", 
    description="API per la telemetria delle moto Ducati", 
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message":"Welcome to Ducati Connect Telemetry API"
    }
