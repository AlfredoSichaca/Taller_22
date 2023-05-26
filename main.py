import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

# Cargar el DataFrame con los datos meteorológicos de Tunja
df = pd.read_csv('datos_tunja.csv', encoding='ISO-8859-1')

# 2. Identificar el tipo de variable de cada columna
print(df.dtypes)

# 3. Calcular los principales valores de las medidas de tendencia central
central_values = df.describe()
print(central_values)

# 4. Graficar una caja de bigotes de los datos de Temperatura
plt.boxplot(df['Temperatura'])
plt.xlabel('Temperatura')
plt.ylabel('Valores')
plt.title('Diagrama de caja de bigotes de Temperatura')
plt.show()



# 5. Calcular las medidas de dispersión
quartiles = np.percentile(df['Temperatura'], [25, 50, 75])
iqr = quartiles[2] - quartiles[0]
std_deviation = df['Temperatura'].std()
variance = df['Temperatura'].var()
print("Cuartiles:", quartiles)
print("Rango intercuartílico:", iqr)
print("Desviación estándar:", std_deviation)
print("Varianza:", variance)

# 6. Mostrar los valores de la serie Temperatura en un array de numpy
temperatura_array = df['Temperatura'].values
print("Valores de Temperatura:", temperatura_array)

# 8. Rango de la Temperatura más frecuente de Tunja
temperatura_mode_range = df['Temperatura'].mode()
print("Rango de la Temperatura más frecuente:", temperatura_mode_range)

quartiles = np.percentile(df['Temperatura'], [25, 50, 75])
iqr = quartiles[2] - quartiles[0]
print("Rango intercuartílico:", iqr)

std_deviation = np.std(df['Temperatura'])
print("Desviación estándar:", std_deviation)

# 10. Cuartil con la mayor cantidad de datos
temperatura_quartiles = pd.qcut(df['Temperatura'], q=4)
quartile_counts = temperatura_quartiles.value_counts()
most_common_quartile = quartile_counts.idxmax()
print("Cuartil con la mayor cantidad de datos:", most_common_quartile)





