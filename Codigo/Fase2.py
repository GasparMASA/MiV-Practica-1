import pandas as pd

class Fase2:
    def __init__(self):
        # Cargamos los datos del .csv
        self.df = pd.read_csv('Csv/salario_minimo_interprofesional.csv', sep=';')

        # Extraemos el ano y el SMI
        self.df['Ano'] = self.df['Fecha de inicio de efectos'].str.extract(r'(\d{4})').astype(int)
        self.df['SMI'] = (self.df['SMI Mes (En euros)'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)).astype(int)
        # 2021 tuvo 2 subidas, nos quedamos con la ultima (como en el grafico original 965€) y reducimos el dataset a 2019 y 2025
        self.df = self.df.drop_duplicates(subset=['Ano'], keep='last')
        self.df = self.df[(self.df['Ano'] >= 2019) & (self.df['Ano'] <= 2025)].copy()

        # 3 - Reconfiguración y ordenación lógica del dataset, Garantizando que el motor gráfico lea el eje temporal correctamente 
        self.df = self.df.sort_values(by='Ano').reset_index(drop=True)

        # 2 - Agrupamiento lógico de variables, separar datos reales de promesas políticas
        self.df['Naturaleza_Dato'] = self.df['Ano'].apply(lambda x: 'Propuesta' if x == 2025 else 'Histórico Consolidado')

        # 1 - Normalizar datos teniendo en cuenta la inflación, permitira ver al especatdor la cifra real.
        tasas_ipc = {2019: 0.8, 2020: -0.3, 2021: 3.1, 2022: 8.4, 2023: 3.5, 2024: 2.8, 2025: 2.0} 
        self.df['IPC_Anual'] = self.df['Ano'].map(tasas_ipc)
        # Formulas de ajuste: Valor Nominal / (1 + (Inflacion / 100))
        self.df['SMI_Poder_Adquisitivo_Real'] = (self.df['SMI'] / (1 + (self.df['IPC_Anual'] / 100))).astype(int)

    # DATOS FINALES
    def ver_datos(self):
        print(self.df[['Ano', 'SMI', 'IPC_Anual', 'SMI_Poder_Adquisitivo_Real', 'Naturaleza_Dato']])

# MAIN
if __name__ == "__main__":
    fase2 = Fase2()
    fase2.ver_datos()