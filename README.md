# MediAssist - AI Medicinski Asistent

MediAssist je AI agent razvijen u Python-u koji pomaze pacijentima da pronadju pravog lekara na osnovu unetih simptoma. Agent koristi LangChain framework i Ollama (llama3.2) jezicki model za analizu simptoma i generisanje preporuka.

Projekat je razvijen kao deo seminarskog rada na predmetu Razvoj naprednih aplikacija u elektronskom poslovanju, Fakultet organizacionih nauka, Univerzitet u Beogradu.

---

## Funkcionalnosti

- Analiza simptoma i preporuka odgovarajuce medicinske specijalnosti
- Preporuka konkretnog lekara sa platforme na osnovu lokacije i specijalnosti
- Dohvatanje informacija o medicinskim specijalnostima putem Wikipedia API-ja
- Detekcija hitnih stanja i upucivanje na hitnu pomoc
- Cuvanje preporuke u JSON ili Markdown formatu
- Validacija korisnickog unosa
- Visekratno koriscenje u okviru jedne sesije

---

## Struktura projekta

ai-agent/

├── agent/

│ ├── init.py

│ ├── agent.py # AI logika i integracija sa LLM modelom

│ ├── data_loader.py # Ucitavanje podataka i Wikipedia API integracija

│ ├── output_handler.py # Generisanje i cuvanje strukturisanog izlaza

│ └── tools.py # Pomocne funkcije

├── data/

│ └── doctors.json # Baza podataka lekara

├── output/ # Generisani izlazni fajlovi

├── prompts/

│ ├── init.py

│ └── system_prompts.py # Sistemski promptovi za LLM model

├── venv/ # Virtualno okruzenje

├── main.py # Ulazna tacka aplikacije

├── requirements.txt # Potrebne biblioteke

└── README.md

---

## Potrebne biblioteke

- langchain
- langchain-ollama
- langchain-core
- requests
- python-dotenv
- pydantic

---

## Pokretanje projekta

### 1. Kloniranje repozitorijuma

```bash
git clone https://github.com/tinaam123/AI-Agent-URIZ-.git
cd ai-agent
```

### 2. Kreiranje i aktivacija virtualnog okruzenja

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalacija potrebnih biblioteka

```bash
pip install langchain langchain-ollama langchain-core requests python-dotenv pydantic
```

### 4. Instalacija i pokretanje Ollama modela

```bash
brew install ollama
ollama serve
```

U novom terminalu:

```bash
ollama pull llama3.2
```

### 5. Pokretanje aplikacije

```bash
python3 main.py
```

---

## Primer koriscenja

Dobrodosli na MediAssist platformu!

# Nasa AI asistent pomaze vam da pronadjete pravog lekara.

MEDIASSIST - AI Medicinski Asistent
Molimo unesite sledece podatke:

(Unesite 'q' u bilo kom trenutku za izlaz)
Ime i prezime: Marko Petrovic

Godine starosti: 35

Simptomi (odvojite zarezom): glavobolja, vrtoglavica

Lokacija (npr. Beograd): Beograd
Analiziram podatke i pretrazujem dostupne lekare...
==================================================

PREPORUKA AI ASISTENTA
PREPORUCENA SPECIJALNOST:

Neurologija
PREPORUCENI LEKAR:

Dr. Marko Nikolic, Beograd, ocena: 4.9
RAZLOG PREPORUKE:

Simptomi kao sto su glavobolja i vrtoglavica najcesce spadaju u domen neurologije.
DOSTUPNI TERMINI:

09:00, 11:00, 14:00
SAVETI ZA PRIPREMU:

Zapisite kada su se simptomi prvi put pojavili
Navedite sve lekove koje trenutno uzimate
Ponecite raniju medicinsku dokumentaciju ukoliko postoji

NAPOMENA:

# Ova preporuka je informativnog karaktera i ne predstavlja medicinsku dijagnozu.

U kom formatu zelite da sacuvate preporuku?

1.JSON
2.Markdown
3.Oba formata
4.Ne zelim da cuvan preporuku

Vas izbor (1-4): 2
Preporuka sacuvana u: output/preporuka_20260614_143022.md
Da li zelite novi upit? (da/ne): ne
Hvala na koriscenju MediAssist platforme. Dovidjenja!

---

## Eksterni podaci i integracije

- **Wikipedia REST API** – dohvatanje informacija o medicinskim specijalnostima
- **doctors.json** – lokalna baza podataka lekara sa dostupnim terminima
