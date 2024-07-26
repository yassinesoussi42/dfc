import streamlit as st
import pandas as pd
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="Projet.F",
    page_icon="data:image/png;base64,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",
    layout="wide")

st.write("Bienvenue sur l'application de filtration de base de données.")

def load_data(file):
    if file is not None:
        file_extension = file.name.split('.')[-1].lower()
        if file_extension == 'csv':
            df = pd.read_csv(file)
        elif file_extension in ['xls', 'xlsx']:
            df = pd.read_excel(BytesIO(file.read()))
        else:
            st.error("Unsupported file format!")
            return None
        return df
    return None

def to_excel(df):
    """Convert DataFrame to Excel file."""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    output.seek(0)
    return output

st.title("Filtration de base de données")

uploaded_file = st.file_uploader("Importer un fichier Excel ", type=["csv", "xls", "xlsx"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    
    if df is not None:
        st.write("### Données importées")
        st.write(df)

        st.sidebar.title("Filtration")
        
        filter_columns = st.sidebar.multiselect("Sélectionnez les colonnes à filtrer", df.columns)
        
        if filter_columns:
            filter_options = {}
            for col in filter_columns:
                unique_values = df[col].dropna().unique()  # Ignorer les valeurs manquantes
                selected_values = st.sidebar.multiselect(f"Valeurs pour {col}", unique_values, format_func=str)
                filter_options[col] = selected_values
            
            # Filtrage des données
            filtered_df = df.copy()
            for col, values in filter_options.items():
                if values:  # Appliquer le filtre seulement si des valeurs sont sélectionnées
                    filtered_df = filtered_df[filtered_df[col].isin(values)]
            
            st.write("### Données filtrées")
            st.write(filtered_df)
            
            # Boutons pour actions sur les données filtrées
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if st.button("Télécharger les données filtrées"):
                    filtered_excel = to_excel(filtered_df)
                    st.download_button(
                        label="Télécharger le fichier Excel",
                        data=filtered_excel,
                        file_name="filtered_data.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            with col2:
                if st.button("Supprimer les valeurs affichées"):
                    # Suppression des valeurs filtrées du DataFrame général
                    df = df[~df.index.isin(filtered_df.index)]
                    
                    st.write("### Données après suppression")
                    st.write(df)
                    
                    # Bouton pour télécharger la version finale
                    final_excel = to_excel(df)
                    st.download_button(
                        label="Télécharger la version finale",
                        data=final_excel,
                        file_name="final_data.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                    
        else:
            st.info("Veuillez sélectionner des colonnes et des valeurs à filtrer.")
else:
    st.info("Veuillez importer un fichier pour commencer.")

