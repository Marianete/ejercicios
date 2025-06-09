import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("users.csv")

# Filtrar top 20 usuarios más viejos del Reino Unido
top_20_uk = df[df["pais"] == "United Kingdom"].sort_values(by="edad", ascending=False).head(20)

# Separar por género
hombres = top_20_uk[top_20_uk["genero"] == "male"]
mujeres = top_20_uk[top_20_uk["genero"] == "female"]

print("Hombres:\n", hombres[["nombre", "edad"]])
print("\nMujeres:\n", mujeres[["nombre", "edad"]])

# Configurar estilo de Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Crear gráfica de barras con Seaborn
ax = sns.barplot(
    x='nombre',
    y='edad',
    hue='genero',
    data=top_20_uk,
    palette={'male': 'blue', 'female': 'pink'},
    order=top_20_uk.sort_values('edad', ascending=False)['nombre']  # Mantener orden original
)

# Personalizar gráfico
plt.title("Top 20 usuarios más viejos del Reino Unido por género", fontsize=14)
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.xticks(rotation=90)
plt.legend(title='Género')

# Ajustar espacio y mostrar
plt.tight_layout()
plt.show()