# 
**Fecha:**  31/03 

---

## 📌 Actividad 1 del Día  
###  
```python
import numpy as np  
import pandas as pd  
b = np.array([[1,2],[3,4],[5,6]])  
a = np.array([0,1,2,3,4,5,6,7,8,9,10])  
print(a, b)  
```

# 
**Fecha:**  01/04 

---

## 📌 Actividad 1 del Día  
### 
```python
import numpy as np  
import pandas as pd  
b = np.array([[1,2],[3,4],[5,6]])  
a = np.array([0,1,2,3,4,5,6,7,8,9,10])  
df = pd.DataFrame(b, index=['FILA1', 'FILA2', 'FILA3'], columns=['COLUMNA1', 'COLUMNA2'])  
provincia = ['Cordoba', 'San Luis', 'Buenos Aires', 'Rioja', 'Tucuman']  
poblacion = [6000000, 5000000, 8000000, 4000000, 1000000 ]   
diccionario = {'Provincia': provincia, 'Poblacion': poblacion}  
df2 = pd.DataFrame(diccionario)  
print(df2)
```
## 📌 Actividad 2 del Día  
###
```python
import pandas as pd     
df = pd.read_csv('StudentsPerformance.csv')  
print (df['gender'])  

#ATRIBUTOS
# .dtypes (tipo de datos de las columnas)
# .shape (cantidad de filas y columnas)
# .mean (muestra la media)
# .min (muestra el minimo)
# .max (muestra el maximo)
# .count (cantidad)

#FUNCIONES 
# .head() - muestra las primeras 5 filas
# .tail() - muestra las ultimas 5 filas 
# .describe() - muestra estadisticas de las columnas numericas 
# .info() - muestra las filas vacias (Tipo de data de nada es: non-null)
# .to_(tipo de dato)() - lo convierte  
# .iloc[:, -3] - mustra las ultimas tres columnas
#ARREGLOs
#['x'] - x=nombre de la columna 
```
# 
**Fecha:**  07/04 

---

## 📌 Actividad 1 del Día  
### Abrir el csv.  Mostrar las columnas gender y mathscore. Mostrar la cantidad dde filas y columnas que tiene.  Mostrar las primeras 4 filas. Mostrar las ultimas 4 lineas. Mostrar la media. Mostrar los tipos de datos de cada columna.
###  
```python
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
print(df[['gender','math score']])
print(df[['gender','math score']].shape)
print(df[['gender','math score']].head(4))
print(df[['gender','math score']].tail(4))
print(df[['gender','math score']].mean)
print(df[['gender','math score']].dtypes)
```
![TERMINAL](https://github.com/Marianete/ejercicios/blob/main/Captura.PNG)
## 📌 Actividad 2 del Día 
### Abrir el csv. Mostar las 3 ultimas columnas. Mostrar las 100 primeras filas. Mostrar la media, minimo, max y cantidad. Convertir al string.
```python
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
print(df[['reading score','math score', 'writing score']])
print(df[['reading score','math score', 'writing score']].head(100))
print(df[['reading score','math score', 'writing score']].mean)
print(df[['reading score','math score', 'writing score']].min)
print(df[['reading score','math score', 'writing score']].max)
print(df[['reading score','math score', 'writing score']].count)
print(df[['reading score','math score', 'writing score']].to_string())
```
![TERMINALL](https://github.com/Marianete/ejercicios/blob/main/Capturanaziii.PNG)

# 
**Fecha:**  08/04 

---

## 📌 Actividad 1 del Día  
### Lo basico en 'matplotlib'
```python
#importar la libreria
import matplotlib.pyplot as plt
#datos
x = [1,2,3,4,5] 
y = [7,77,89,23,21]
#crear graficos
plt.plot(x,y)
#etiquetas
plt.xlabel('eje x')
plt.ylabel('eje y')
#titulear
plt.title('Grafico de ejemplo')
#mostrar
plt.show()
```
```python
import matplotlib.pyplot as plt
datos = [40,40,10,10]
color = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
label = ['Gatos','Perros','Delfines','Pajaros']
plt.pie(datos, labels= label, colors= color, autopct= '%1.1f%%', startangle= 140)
plt.title('grafico de torta')
plt.axis('equal')
plt.show()
```
```python
import matplotlib.pyplot as plt
import pandas as pd 
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,5,8,11,14,17,20,23,26,29]
plt.scatter(x,y,color= 'blue', marker= 'o')
plt.title('Grafico de dispercion')
plt.xlabel('Hola')
plt.ylabel('Hola')
plt.show()
```

