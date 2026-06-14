import sys
from agent import (analyze_appointment, get_doctor_info, validate_patient_data,
                   format_recommendation, save_as_json, save_as_markdown)

def get_user_input() -> dict:
    print("\n" + "="*50)
    print("MEDIASSIST - AI Medicinski Asistent")
    print("="*50)
    print("\nMolimo unesite sledece podatke:")
    print("(Unesite 'q' u bilo kom trenutku za izlaz)\n")

    fields = {
        "name": "Ime i prezime: ",
        "age": "Godine starosti: ",
        "symptoms": "Simptomi (odvojite zarezom): ",
        "location": "Lokacija (npr. Beograd): "
    }

    patient_data = {}

    for field, prompt in fields.items():
        while True:
            value = input(prompt).strip()

            if value.lower() == 'q':
                print("\nHvala na koriscenju MediAssist platforme. Dovidjenja!")
                sys.exit(0)

            if not value:
                print("Greska: Ovo polje je obavezno. Pokusajte ponovo.")
                continue

            if field == "age":
                try:
                    age = int(value)
                    if age < 0 or age > 120:
                        print("Greska: Unesite validne godine (0-120).")
                        continue
                except ValueError:
                    print("Greska: Godine moraju biti broj.")
                    continue

            patient_data[field] = value
            break

    return patient_data

def ask_save_output() -> str:
    """Pita korisnika u kom formatu zeli da sacuva rezultat"""
    print("\nU kom formatu zelite da sacuvate preporuku?")
    print("1. JSON")
    print("2. Markdown")
    print("3. Oba formata")
    print("4. Ne zelim da cuvan preporuku")

    while True:
        choice = input("\nVas izbor (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Greska: Unesite broj od 1 do 4.")

def display_result(result: dict):
    print("\n" + "="*50)
    print("PREPORUKA AI ASISTENTA")
    print("="*50)
    print(result["recommendation"])
    print("="*50)

def ask_continue() -> bool:
    while True:
        choice = input("\nDa li zelite novi upit? (da/ne): ").strip().lower()
        if choice in ['da', 'd']:
            return True
        elif choice in ['ne', 'n']:
            return False
        print("Molimo unesite 'da' ili 'ne'.")

def main():
    print("\nDobrodosli na MediAssist platformu!")
    print("Nasa AI asistent pomaze vam da pronadjete pravog lekara.")

    while True:
        try:
            patient_data = get_user_input()

            if not validate_patient_data(patient_data):
                print("\nGreska: Sva polja su obavezna. Pokusajte ponovo.")
                continue

            print("\nAnaliziram podatke i pretrazujem dostupne lekare...")
            recommendation = analyze_appointment(patient_data)
            result = format_recommendation(recommendation)

            display_result(result)

            choice = ask_save_output()

            if choice == '1':
                path = save_as_json(patient_data, recommendation)
                print(f"\nPreporuka sacuvana u: {path}")
            elif choice == '2':
                path = save_as_markdown(patient_data, recommendation)
                print(f"\nPreporuka sacuvana u: {path}")
            elif choice == '3':
                json_path = save_as_json(patient_data, recommendation)
                md_path = save_as_markdown(patient_data, recommendation)
                print(f"\nPreporuka sacuvana u: {json_path}")
                print(f"Preporuka sacuvana u: {md_path}")

            if not ask_continue():
                print("\nHvala na koriscenju MediAssist platforme. Dovidjenja!")
                break

        except KeyboardInterrupt:
            print("\n\nProgram prekinut. Dovidjenja!")
            sys.exit(0)

if __name__ == "__main__":
    main()