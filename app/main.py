import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(title="Taller AWS - FastAPI")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://admin:TU_PASSWORD@TU_ENDPOINT_RDS:3306/taller_fastapi"
)

engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"mensaje": "La API está funcionando correctamente 🚀"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {
            "status": "ok",
            "database": "conectada",
            "mensaje": "La conexión a RDS está funcionando"
        }
    except Exception as e:
        return {
            "status": "error",
            "database": "desconectada",
            "detalle": str(e)
        }