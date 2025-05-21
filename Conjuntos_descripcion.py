import csv
import pandas as pd

# Leer CSV como texto para evitar que pandas cambie los tipos
# Leer ambos archivos CSV
df_base = pd.read_csv('/home/ailan/Trabajo/catalago/#128561/conjuntos_de_ datos.csv', dtype=str, quotechar='"', sep=',', encoding='utf-8')  # contiene las columnas: ID, title, etc.
df_catalogo = pd.read_csv('/home/ailan/Trabajo/catalago/#128561/datasets_catalogo.csv', dtype=str, quotechar='"', sep=',', encoding='utf-8')  # contiene: ID, Descripción

# Crear diccionario ID → Descripción
desc_dict = df_catalogo.set_index('ID')['Descripción'].to_dict()

# Insertar descripción con texto por defecto si no hay
df_base.insert(3, 'Descripción', df_base['ID'].map(desc_dict))

# Guardar asegurando que todas las celdas van entre comillas
df_base.to_csv(
    'conjuntos_datos_con_descripcion_2.csv',
    index=False,
    quoting=csv.QUOTE_ALL,  # 👈 clave para evitar que se desplacen columnas
    quotechar='"',
    encoding='utf-8'
)