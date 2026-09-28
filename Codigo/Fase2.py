import pandas as pd

# Cargamos los datos del .csv
df = pd.read_csv('Csv/salario_minimo_interprofesional.csv', sep=';')

# Extraemos el ano y el SMI
df['Ano'] = df['Fecha de inicio de efectos'].str.extract(r'(\d{4})').astype(int)
df['SMI'] = (df['SMI Mes (En euros)'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)).astype(int)
# 2021 tuvo 2 subidas, nos quedamos con la ultima (como en el grafico original 965€) y reducimos el dataset a 2019 y 2025
df = df.drop_duplicates(subset=['Ano'], keep='last')
df = df[(df['Ano'] >= 2019) & (df['Ano'] <= 2025)].copy()

# 3 - Reconfiguración y ordenación lógica del dataset, Garantizando que el motor gráfico lea el eje temporal correctamente 
df = df.sort_values(by='Ano').reset_index(drop=True)

# 2 - Agrupamiento lógico de variables, separar datos reales de promesas políticas
df['Naturaleza_Dato'] = df['Ano'].apply(lambda x: 'Propuesta' if x == 2025 else 'Histórico Consolidado')

# 1 - Normalizar datos teniendo en cuenta la inflación, permitira ver al especatdor la cifra real.
tasas_ipc = {2019: 0.8, 2020: -0.3, 2021: 3.1, 2022: 8.4, 2023: 3.5, 2024: 2.8, 2025: 2.0} 
df['IPC_Anual'] = df['Ano'].map(tasas_ipc)
# Formulas de ajuste: Valor Nominal / (1 + (Inflacion / 100))
df['SMI_Poder_Adquisitivo_Real'] = (df['SMI'] / (1 + (df['IPC_Anual'] / 100))).astype(int)

# DATOS FINALES
print(df[['Ano', 'SMI', 'IPC_Anual', 'SMI_Poder_Adquisitivo_Real', 'Naturaleza_Dato']])