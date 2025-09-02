import json
import os

# Load maintenance schedules from JSON files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

def load_maintenance_schedule(car_model: str) -> dict:
    file_path = os.path.join(DATA_DIR, f"{car_model.lower()}_schedule.json")
    if not os.path.exists(file_path):
        return {"error": f"No maintenance schedule found for {car_model}"}

    with open(file_path, "r") as f:
        return json.load(f)

def get_maintenance_advice(car_model: str, kms: int) -> str:
    schedule = load_maintenance_schedule(car_model)
    if "error" in schedule:
        return schedule["error"]

    due_tasks = [task for km, task in schedule.items() if kms >= int(km)]
    if not due_tasks:
        return "No maintenance needed yet."
    
    return f"Recommended tasks for {car_model} at {kms} km: {', '.join(due_tasks)}"
