from fastapi import APIRouter
from app.models.car import SymptomReport, DiagnosisResponse
from app.services.diagnostic_service import diagnose

router = APIRouter(prefix="/diagnostics", tags=["diagnostics"])

@router.post("/diagnose", response_model=DiagnosisResponse)
async def diagnose_endpoint(payload: SymptomReport) -> DiagnosisResponse:
    top = diagnose(payload)
    return DiagnosisResponse(top_candidates=top)