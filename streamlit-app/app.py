import streamlit as st
import pandas as pd
import requests 

# ETL
def extract(pokemon_name):
    
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'       
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error('Wrong Name, Baka!', icon='😵')


def transform(data):
     
        abilities = [a['ability']['name'] for a in data.get('abilities', [])]      
        picture = data['sprites']['other']['official-artwork']['front_default']
        cries = data['cries']['latest']

        required_data = {
            'ID': data['id'],
            'Name': data['name'],
            'Image': picture,
            'Cries': cries,
            'Height': data['height'],
            'Weight': data['weight'],
            'XP': data['base_experience'],
            'Abilities': ', '.join(abilities)
        }

        transformed_data = pd.DataFrame([required_data])

        if not transformed_data.empty:
            st.success("Data successfully fetched.")

        return transformed_data


def load(transformed_data):
    st.success('Pokemon data loaded successfully!')
    st.subheader('Pokemon Details:')

    if transformed_data['Image'][0]:
        st.image(transformed_data['Image'][0], width=300)

    if transformed_data['Cries'][0]:
        if st.button('Pokemon Cry'):
            st.audio(transformed_data['Cries'][0], format='audio/ogg')

    st.table(transformed_data.drop(columns=['Image', 'Cries']))


# Streamlit App
st.title('Welcome to PokeDex⚡')
pokemon_name = st.text_input('Enter name of pokemon: ').lower()

if pokemon_name:
    extracted_data = extract(pokemon_name)

    if extracted_data:
        transformed_data = transform(extracted_data)
        load(transformed_data)
