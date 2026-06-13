def format_recommendation(recommendation: str) -> dict:
    return {
        "status": "success",
        "recommendation": recommendation
    }

def validate_patient_data(data: dict) -> bool:
    required_fields = ["name", "symptoms", "age"]
    return all(field in data and data[field] for field in required_fields)