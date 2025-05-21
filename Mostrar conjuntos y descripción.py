import requests
import csv

BASE_URL = "https://catalogodatos.gub.uy/api/3/action"

# 1. Obtener todos los IDs de conjuntos
response = requests.get(f"{BASE_URL}/package_list")
ids = response.json()['result']

# 2. Lista para guardar los datos de salida
datasets_info = []

# 3. Por cada ID, obtener detalles
for dataset_id in ids:
    details = requests.get(f"{BASE_URL}/package_show", params={'id': dataset_id})
    if details.status_code == 200:
        result = details.json().get('result', {})
        datasets_info.append({
            'ID': result.get('id', ''),
            'Nombre': result.get('title', ''),
            'Descripción': result.get('notes', '')
        })

# 4. Escribir CSV
csv_path = '/home/ailan/Trabajo/catalago/#128561/datasets_catalogo_2.csv'
with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ID', 'Nombre', 'Descripción']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(datasets_info)

csv_path
