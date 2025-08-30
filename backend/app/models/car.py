from pydantic import BaseModel, Field
from typing import List, Optional

class VehicleInfo(BaseModel):
    make: str
    model: str
    year: int
    fuel_type: str = Field(description="petrol|diesel|electric|hybrid|cng|lpg")

class SymptomReport(BaseModel):
    vehicle: VehicleInfo
    odometer_km: Optional[int] = Field(default=None, ge=0)
    description: str

class DiagnosisCandidate(BaseModel):
    issue: str
    confidence: float = Field(ge=0, le=1)
    next_steps: str

class DiagnosisResponse(BaseModel):
    top_candidates: List[DiagnosisCandidate]

class MaintenanceRequest(BaseModel):
    vehicle: VehicleInfo
    odometer_km: int

class MaintenanceItem(BaseModel):
    task: str
    interval_km: int
    due_at_km: int
    status: str  # OVERDUE | DUE_NOW | COMING_SOON | OK
    notes: Optional[str] = None

class MaintenanceResponse(BaseModel):
    items: List[MaintenanceItem]

class TipsRequest(BaseModel):
    vehicle: VehicleInfo
    context: Optional[str] = None  # e.g., monsoon, summer, battery

class Tip(BaseModel):
    title: str
    detail: str

class TipsResponse(BaseModel):
    tips: List[Tip]