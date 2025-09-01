# PokéAPI Pipeline ⚡

This ETL pipeline is built using the [PokéAPI](https://pokeapi.co/).  

## 🔹 Version 1: Manual ETL (API Pipeline)

Fetches Pokémon data using the PokéAPI, and loads it into MySQL Workbench.  

### ETL Flow:  
- **Extract → Transform → Load** are internally connected in the script.  
- You only need to **run the load function**, which automatically performs extraction and transformation before saving the final dataset.

### Steps to Run:

```bash
cd manual-version
python load.py
```

## 🔸 Version 2: Streamlit Pokédex App

An interactive Pokédex where users can search Pokémon by name, and view details.  

### Features:
- User enters Pokémon name in a text field.  
- App fetches data from PokéAPI in real time.  
- Displays Pokémon ID, name, abilities, height, weight, image and play audio button(Pokémon cry).    

### Steps to Run:

```bash
cd streamlit-app
streamlit run app.py
```