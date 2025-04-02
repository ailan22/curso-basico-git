import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill

# Cargar archivos CSV
conjuntos = pd.read_csv("/home/ailan/Downloads/conjuntos.csv")  # Contiene columna: 'creator_user_name'
usuarios = pd.read_csv("/home/ailan/Downloads/usuarios.csv")    # Contiene columna: 'name'

# Verificar qué usuarios tienen conjuntos creados
usuarios["tiene_conjunto"] = usuarios["name"].isin(conjuntos["creator_user_name"])

# Crear un archivo Excel con colores
archivo_salida = "usuarios_con_color.xlsx"
with pd.ExcelWriter(archivo_salida, engine="openpyxl") as writer:
    usuarios.to_excel(writer, sheet_name="Usuarios", index=False)

    # Cargar el archivo para aplicar colores
    wb = writer.book
    ws = wb["Usuarios"]

    # Definir colores
    fill_verde = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")  # Verde
    fill_blanco = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")  # Blanco (sin color)

    # Aplicar colores fila por fila
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        usuario = row[0].value  # Primera columna (name)
        if usuario in conjuntos["creator_user_name"].values:
            fill = fill_verde
        else:
            fill = fill_blanco
        for cell in row:
            cell.fill = fill

    # Guardar cambios
    wb.save(archivo_salida)

print(f"Archivo generado: {archivo_salida}")
