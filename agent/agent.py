from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

def create_llm():
    return ChatOllama(
        model="llama3.2",
        temperature=0.7
    )

def analyze_appointment(patient_data: dict) -> str:
    llm = create_llm()
    
    messages = [
        SystemMessage(content="""Ti si medicinski asistent na platformi za zakazivanje pregleda. 
        Pomažeš pacijentima da pronađu pravog lekara i zakažu pregled na osnovu njihovih simptoma."""),
        HumanMessage(content=f"""
        Pacijent ima sledeće informacije:
        - Ime: {patient_data['name']}
        - Simptomi: {patient_data['symptoms']}
        - Starost: {patient_data['age']}
        
        Preporuči odgovarajuću specijalnost lekara i savete za pripremu pregleda.
        """)
    ]
    
    response = llm.invoke(messages)
    return response.content