from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from agent.data_loader import load_doctors, get_specialty_info, find_doctors_by_specialty, suggest_specialty
from prompts.system_prompt import SYSTEM_PROMPT, URGENCY_PROMPT, USER_PROMPT_TEMPLATE

URGENT_SYMPTOMS = [
    "bol u grudima", "otežano disanje", "gubitak svesti",
    "paraliza", "jak bol u stomaku"
]

def create_llm():
    return ChatOllama(
        model="llama3.2",
        temperature=0.7
    )

def check_urgency(symptoms: str) -> bool:
    """Proverava da li simptomi ukazuju na hitno stanje"""
    symptoms_lower = symptoms.lower()
    return any(symptom in symptoms_lower for symptom in URGENT_SYMPTOMS)

def analyze_appointment(patient_data: dict) -> str:
    llm = create_llm()

    if check_urgency(patient_data['symptoms']):
        return URGENCY_PROMPT

    suggested_specialty = suggest_specialty(patient_data['symptoms'])
    
    doctors = load_doctors()
    matching_doctors = find_doctors_by_specialty(suggested_specialty)
    
    doctors_info = "\n".join([
        f"- {d['name']} ({d['specialty']}, {d['location']}, ocena: {d.get('rating', 'N/A')}, termini: {', '.join(d.get('available_slots', []))})"
        for d in matching_doctors
    ]) if matching_doctors else "Trenutno nema dostupnih lekara ove specijalnosti."

    specialty_info = get_specialty_info(suggested_specialty)

    user_prompt = USER_PROMPT_TEMPLATE.format(
        name=patient_data['name'],
        age=patient_data['age'],
        symptoms=patient_data['symptoms'],
        location=patient_data['location'],
        doctors_info=doctors_info,
        specialty_info=specialty_info
    )

    messages = [
        SystemMessage(content=SYSTEM_PROMPT + f"\n\nNa osnovu analize simptoma, preporucena specijalnost je: {suggested_specialty}. Koristi ovu specijalnost u svom odgovoru."),
        HumanMessage(content=user_prompt)
    ]

    response = llm.invoke(messages)
    return response.content

def get_doctor_info(specialty: str) -> dict:
    wiki_info = get_specialty_info(specialty)
    available_doctors = find_doctors_by_specialty(specialty)
    return {
        "specialty_info": wiki_info,
        "available_doctors": available_doctors
    }