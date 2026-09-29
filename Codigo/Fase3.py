from Fase2 import Fase2
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Inicializamos los datos de la fase 2
f2 = Fase2()
# f2.ver_datos()

#Cuadricula
grafico = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "xy"}, {"type": "polar"}]],
    subplot_titles=("Comparativa en Líneas Evolución del Salario Mínimo Interprofesional (2019-2025)", "Comparativa en Radar Evolución del Salario Mínimo Interprofesional (2019-2025)")
)

#------------------------------------------------------------------------------
#Grafico de lineas
# 1: SMI Nominal (Enganoso)
grafico.add_trace(go.Scatter(
    x=f2.df['Ano'], 
    y=f2.df['SMI'],
    mode='lines+markers',
    name='SMI Nominal (Sin ajustar)',
    line=dict(color='#e74c3c', width=2, dash='dot'),
    marker=dict(size=8)
), row=1, col=1)
# 2: SMI Real
grafico.add_trace(go.Scatter(
    x=f2.df['Ano'], 
    y=f2.df['SMI_Poder_Adquisitivo_Real'],
    mode='lines+markers',
    name='SMI Real (Ajustado a la Inflación)',
    line=dict(color='#27ae60', width=4),
    marker=dict(size=10)
), row=1, col=1)
#------------------------------------------------------------------------------
#Grafico de radar
anos = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']
grafico.add_trace(go.Scatterpolar(
    #Valores de la grafica enganosa
    r=f2.df['SMI'],
    theta=anos,
    fill='toself',
    name='SMI nominal Enganoso'
), row=1, col=2)
grafico.add_trace(go.Scatterpolar(
    #Valores ajustados
    r=f2.df['SMI_Poder_Adquisitivo_Real'],
    theta=anos,
    fill='toself',
    name='SMI real'
), row=1, col=2)
#------------------------------------------------------------------------------

# Mostrar Grafico de lineas
grafico.update_yaxes(rangemode='tozero', row=1, col=1)
grafico.show()