import pandas as pd

# Definir los datos
data = {
    'Estacion': ['Estacion_A', 'Estacion_B', 'Estacion_C', 'Estacion_D'],
    'Flujo_Pasajeros': [300, 150, 400, 250],
    'Tiempo_Espera_Minutos': [5, 10, 7, 12],
    'Frecuencia_Servicios': [6, 4, 5, 3],
    'Distancia_km': [0, 5, 3, 7]  # Distancia a la siguiente estación
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Guardar el DataFrame como CSV
df.to_csv('transporte_masivo_data_no_supervisado.csv', index=False)

print("Archivo transporte_masivo_data_no_supervisado.csv generado correctamente.")
