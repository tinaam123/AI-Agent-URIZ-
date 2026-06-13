from agent import analyze_appointment, format_recommendation, validate_patient_data

def main():
    print("=== Platforma za zakazivanje medicinskih pregleda - AI Asistent ===\n")
    
    patient_data = {
        "name": input("Unesite ime pacijenta: "),
        "age": input("Unesite godine pacijenta: "),
        "symptoms": input("Unesite simptome: ")
    }
    
    if not validate_patient_data(patient_data):
        print("Greška: Sva polja su obavezna.")
        return
    
    print("\nAnaliziram podatke...")
    recommendation = analyze_appointment(patient_data)
    result = format_recommendation(recommendation)
    
    print("\n=== Preporuka AI asistenta ===")
    print(result["recommendation"])

if __name__ == "__main__":
    main()