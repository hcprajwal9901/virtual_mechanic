from fastapi import APIRouter
from datetime import datetime
from app.models.car import TipsRequest, TipsResponse, Tip

router = APIRouter(prefix="/tips", tags=["tips"])

BASE_TIPS = {
    "petrol": [
        ("Fuel quality", "Stick to trusted pumps; bad fuel causes knocking and rough idle."),
        ("Spark plugs", "Inspect/replace ~20k–40k km for smooth starts and mileage."),
    ],
    "diesel": [
        ("Warm-up", "Allow a short idle after cold start; protects turbo and injectors."),
        ("DPF care", "Regular highway runs help passive regeneration and prevent clogging."),
    ],
    "electric": [
        ("Battery SOC", "Keep between 20%–80% for longevity; avoid frequent 100% charges."),
        ("Tyres", "Instant torque wears tyres faster—check pressures monthly."),
    ],
}

@router.post("/suggest", response_model=TipsResponse)
async def suggest_tips(req: TipsRequest) -> TipsResponse:
    fuel = req.vehicle.fuel_type.lower()
    tips = [Tip(title=t[0], detail=t[1]) for t in BASE_TIPS.get(fuel, [])]

    # Seasonal hint (very simple demo)
    month = datetime.utcnow().month
    if month in (6, 7, 8, 9):
        tips.append(Tip(title="Monsoon care", detail="Check wipers, tyre tread depth (≥3mm), and brake bite."))
    else:
        tips.append(Tip(title="Heat care", detail="Top up coolant, check AC performance and cabin filter."))

    return TipsResponse(tips=tips)