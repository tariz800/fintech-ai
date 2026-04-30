from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="FinSight AI",
    description="Autonomous Credit Underwriting Platform",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok",
            "service": "finsight-ai",
            "version": "0.1.0",
            "environment": os.getenv("APP_ENV", "development")
            }


@app.get("/")
def root():
    return {
        "message":"FinSight AI - Autonomous Credit Underwriting Platform",
        "docs":"/docs"
    }