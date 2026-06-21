import json
import requests
import os

def load_doctors() -> list:
    """Ucitava listu lekara iz lokalnog JSON fajla"""
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'doctors.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['doctors']

def get_specialty_info(specialty: str) -> str:
    """Dohvata informacije o medicinskoj specijalnosti sa Wikipedia API-ja"""
    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/"
        
        specialty_map = {
            "kardiologija": "Cardiology",
            "neurologija": "Neurology",
            "dermatologija": "Dermatology",
            "pulmologija": "Pulmonology",
            "opšta praksa": "General_practitioner"
        }
        
        english_term = specialty_map.get(specialty.lower(), specialty)
        response = requests.get(url + english_term, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('extract', 'Nema dostupnih informacija.')
        return "Nema dostupnih informacija sa Wikipedia-e."
    
    except requests.RequestException:
        return "Nije moguće dohvatiti informacije u ovom trenutku."

def find_doctors_by_specialty(specialty: str) -> list:
    """Filtrira lekare po specijalnosti"""
    doctors = load_doctors()
    return [
        doc for doc in doctors
        if specialty.lower() in doc['specialty'].lower()
    ]

SYMPTOM_SPECIALTY_MAP = {
    "glavobolja": "neurologija",
    "vrtoglavica": "neurologija",
    "nesanica": "neurologija",
    "trnjenje": "neurologija",
    "bol u grudima": "kardiologija",
    "lupanje srca": "kardiologija",
    "visok pritisak": "kardiologija",
    "otezano disanje": "pulmologija",
    "kasalj": "pulmologija",
    "gusenje": "pulmologija",
    "osip": "dermatologija",
    "svrab": "dermatologija",
    "akne": "dermatologija",
    "promena na kozi": "dermatologija",
    "stomacni bol": "opšta praksa",
    "temperatura": "opšta praksa",
    "umor": "opšta praksa"
}

def suggest_specialty(symptoms: str) -> str:
    """Mapira simptome na odgovarajucu specijalnost na osnovu kljucnih reci"""
    symptoms_lower = symptoms.lower()
    
    for keyword, specialty in SYMPTOM_SPECIALTY_MAP.items():
        if keyword in symptoms_lower:
            return specialty
    
    return "opšta praksa"