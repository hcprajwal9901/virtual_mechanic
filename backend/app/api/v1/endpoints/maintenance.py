from fastapi import APIRouter
from app.models.car import MaintenanceRequest, MaintenanceResponse, MaintenanceItem
from pathlib import Path
import json

router = APIRouter(prefix="/maintenance", tags=["maintenance"])
DATA_DIR = Path(__file__).resolve().parents[5] / "data" / "maintenance_schedules"

GENERIC = [
    {"task": "Engine oil & filter", "interval_km": 10000, "notes": "Use spec oil"},
    {"task": "Tyre rotation/balance", "interval_km": 10000, "notes": "Cross-rotate if applicable"},
    {"task": "Air filter replace", "interval_km": 20000},
    {"task": "Cabin filter replace", "interval_km": 20000},
    {"task": "Brake fluid replace", "interval_km": 40000},
    {"task": "Coolant inspect/replace", "interval_km": 50000},
]

def load_schedule(make: str, model: str, year: int):
    fname = f"{make.lower()}_{model.lower()}_{year}.json".replace(" ", "_")
    path = DATA_DIR / fname
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return GENERIC

@router.post("/due", response_model=MaintenanceResponse)
async def maintenance_due(req: MaintenanceRequest) -> MaintenanceResponse:
    tasks = load_schedule(req.vehicle.make, req.vehicle.model, req.vehicle.year)
    items = []
    km = req.odometer_km

    for t in tasks:
        interval = int(t["interval_km"])
        due_at = (km // interval) * interval  # last interval boundary
        status = "OK"
        if km >= due_at and (km - due_at) < 1000:
            status = "DUE_NOW"
        if km - due_at >= 1000:
            status = "OVERDUE"
        if (due_at - km) > 0 and (due_at - km) <= 2000:
            status = "COMING_SOON"
        items.append(MaintenanceItem(task=t["task"], interval_km=interval, due_at_km=due_at, status=status, notes=t.get("notes")))

    return MaintenanceResponse(items=items)
