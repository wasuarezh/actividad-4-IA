from sklearn.cluster import KMeans
import pandas as pd

# Cargar los datos
df = pd.read_csv('transporte_masivo_data_no_supervisado.csv')

# Seleccionar características para el clustering
X = df[['Flujo_Pasajeros', 'Tiempo_Espera_Minutos', 'Frecuencia_Servicios']]

# Crear el modelo KMeans
kmeans = KMeans(n_clusters=2)  # Cambiar el número de clusters según sea necesario

# Ajustar el modelo
kmeans.fit(X)

# Predecir los clusters
df['Cluster'] = kmeans.labels_

# Mostrar el resultado
print(df)
