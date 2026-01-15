import pandas as pd
import csv

# Leer CSV como texto para evitar que pandas cambie los tipos
# Leer ambos archivos CSV
df_base = pd.read_csv('/home/ailan/Trabajo/catalago/#128561/conjuntos_de_datos.csv', dtype=str, encoding='utf-8')  # contiene las columnas: ID, title, etc.
df_catalogo = pd.read_csv('/home/ailan/Trabajo/catalago/#128561/datasets_catalogo_description.csv', dtype=str, encoding='utf-8')  # contiene: ID, Descripción

# Crear diccionario ID → Descripción
desc_dict = df_catalogo.set_index('ID')['Descripción'].to_dict()

# Insertar descripción con texto por defecto si no hay
df_base.insert(3, 'Descripción', df_base['ID'].map(desc_dict))

# Guardar asegurando que todas las celdas van entre comillas
df_base.to_csv('archivo_final.csv', index=False, encoding='utf-8', quoting=csv.QUOTE_ALL)