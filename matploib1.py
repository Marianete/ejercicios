import matplotlib.pyplot as plt

# Datos
dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie']
temperaturas = [22, 24, 21, 23, 25]  # en °C

# Crear gráfico de línea simple
plt.plot(dias, temperaturas, marker='o')

# Etiquetas y título
plt.xlabel('Día de la semana')
plt.ylabel('Temperatura (°C)')
plt.title('Temperaturas promedio de lunes a viernes')

# Mostrar cuadrícula para contexto
plt.grid(True)
plt.tight_layout()
plt.show()
