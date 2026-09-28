from Fase2 import Fase2
import plotly.graph_objects as go

# Inicializamos los datos de la fase 2
f2 = Fase2()
# f2.ver_datos()

# Inicializamos la figura
fig = go.Figure()

# 1: SMI Nominal (Engañoso)
fig.add_trace(go.Scatter(
    x=f2.df['Ano'], 
    y=f2.df['SMI'],
    mode='lines+markers',
    name='SMI Nominal (Sin ajustar)',
    line=dict(color='#e74c3c', width=2, dash='dot'),
    marker=dict(size=8)
))

# 2: SMI Real
fig.add_trace(go.Scatter(
    x=f2.df['Ano'], 
    y=f2.df['SMI_Poder_Adquisitivo_Real'],
    mode='lines+markers',
    name='SMI Real (Ajustado a la Inflación)',
    line=dict(color='#27ae60', width=4),
    marker=dict(size=10)
))

# Configuración interactiva y corrección de principios de Tufte
fig.update_layout(
    title='Evolución del Salario Mínimo Interprofesional (2019-2025)',
    xaxis_title='Ano',
    yaxis_title='Euros (€)',
    yaxis=dict(rangemode='tozero'), # Eje Y a empieza en 0
    hovermode='x unified',          # Activa el tooltip comparativo
    template='plotly_white',        # Elimina fondos basura
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

# Mostrar Grafico
fig.show()