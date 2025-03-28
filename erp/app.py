import sys
print("DEBUG: sys.executable:", sys.executable)
print("DEBUG: sys.path:", sys.path)
from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Dict, Any
from erp.core.erp_system import initialize_erp_system

app = FastAPI(title="ERP Framework API", description="FastAPI based ERP API")

# Define Pydantic models for API endpoints (separate from domain models)
class SalesRequest(BaseModel):
    order_id: str

class ApiResponse(BaseModel):
    result: str

erp_system = initialize_erp_system()

@app.get("/")
def read_root():
    return "Welcome to the ERP Framework API"

@app.post("/api/process/sales", response_model=ApiResponse)
def process_sales(payload: SalesRequest):
    result = erp_system.process("sales", payload.dict())
    return ApiResponse(result=result)

@app.post("/api/process/{module}", response_model=ApiResponse)
def process_module(module: str = Path(...), payload: Dict[str, Any] = {}):
    result = erp_system.process(module, payload)
    return ApiResponse(result=result)
