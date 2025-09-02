"""
Very simple rule-based diagnostic engine for MVP.
Replace with ML/Bayesian later.
"""
from typing import List
from app.models.car import SymptomReport, DiagnosisCandidate

COMMON_RULES = [
    # Won't start
    ("won't start", "Dead/weak battery", 0.75, "Check if interior/dash lights are dim. Try a jump start."),
    ("no crank", "Starter motor issue", 0.6, "Listen for single click; if yes, starter/solenoid may be bad."),
    ("clicking", "Weak battery or corroded terminals", 0.65, "Inspect battery terminals, clean and tighten."),

    # Noises
    ("squeal", "Worn/loose serpentine belt", 0.7, "Inspect belt tension and condition; replace if glazed/cracked."),
    ("rattle", "Loose heat shield or suspension bushing", 0.55, "Check exhaust heat shields and front suspension links."),
    ("clunk", "Stabilizer link or ball joint wear", 0.6, "Inspect sway bar links/ball joints over bumps."),

    # Smoke/Smell
    ("burning smell", "Oil leak onto hot components", 0.5, "Check valve cover gasket and look for oil drips."),
    ("black smoke", "Running rich (petrol) / injector issue (diesel)", 0.55, "Scan fuel trims/injectors; air filter condition."),

    # Overheating
    ("overheat", "Low coolant or failing thermostat", 0.6, "Check coolant level, fans, and thermostat operation."),
]

FUEL_BIASES = {
    "diesel": {
        "black smoke": ("Injector/DPF related", 0.7, "Check DPF status and injector spray pattern."),
        "hard start": ("Glow plug or fuel pressure", 0.6, "Test glow plugs; check rail pressure."),
    },
    "electric": {
        "won't start": ("12V auxiliary battery low", 0.65, "Check 12V battery; EVs rely on it to boot systems."),
    },
}

def diagnose(report: SymptomReport) -> List[DiagnosisCandidate]:
    desc = report.description.lower().strip()
    candidates: List[DiagnosisCandidate] = []

    # Base rules
    for needle, issue, conf, steps in COMMON_RULES:
        if needle in desc:
            candidates.append(DiagnosisCandidate(issue=issue, confidence=conf, next_steps=steps))

    # Fuel-specific hints
    fuel = report.vehicle.fuel_type.lower()
    if fuel in FUEL_BIASES:
        for needle, (issue, conf, steps) in FUEL_BIASES[fuel].items():
            if needle in desc:
                candidates.append(DiagnosisCandidate(issue=issue, confidence=conf, next_steps=steps))

    # Odometer heuristics
    if report.odometer_km is not None:
        km = report.odometer_km
        if km >= 80000 and ("clunk" in desc or "rattle" in desc):
            candidates.append(DiagnosisCandidate(
                issue="Wear in suspension components",
                confidence=0.6,
                next_steps="Inspect control arm bushings, struts, and sway bar links."
            ))

    # Default fallback if nothing matched
    if not candidates:
        candidates.append(DiagnosisCandidate(
            issue="General inspection required",
            confidence=0.3,
            next_steps="Collect more specifics: when it happens, noises, lights, leaks."
        ))

    # Ensure max 3 results sorted by confidence
    candidates.sort(key=lambda c: c.confidence, reverse=True)
    return candidates[:3]
