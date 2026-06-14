import json
import os
from datetime import datetime

OUTPUT_DIR = "output"

def ensure_output_dir():
    """Kreira output folder ako ne postoji"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def save_as_json(patient_data: dict, recommendation: str) -> str:
    """Cuva rezultat u JSON fajl"""
    ensure_output_dir()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/preporuka_{timestamp}.json"
    
    output = {
        "timestamp": datetime.now().isoformat(),
        "patient": {
            "name": patient_data["name"],
            "age": patient_data["age"],
            "location": patient_data["location"],
            "symptoms": patient_data["symptoms"]
        },
        "recommendation": recommendation,
        "status": "success"
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    
    return filename

def save_as_markdown(patient_data: dict, recommendation: str) -> str:
    """Cuva rezultat u Markdown fajl"""
    ensure_output_dir()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/preporuka_{timestamp}.md"
    
    content = f"""# MediAssist - Preporuka lekara

## Podaci o pacijentu

| Polje      | Vrednost                  |
|------------|---------------------------|
| Ime        | {patient_data["name"]}    |
| Godine     | {patient_data["age"]}     |
| Lokacija   | {patient_data["location"]}|
| Simptomi   | {patient_data["symptoms"]}|

## Preporuka AI asistenta

{recommendation}

---
*Generisano: {datetime.now().strftime("%d.%m.%Y u %H:%M")}*
*MediAssist platforma - Sve preporuke su iskljucivo informativnog karaktera.*
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename