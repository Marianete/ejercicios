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
# 
**Fecha:**  14/04 

---

## 📌 Actividad 1 del Día  
### 
```python
import pandas as pd 
import numpy as np
df = pd.read_csv('StudentsPerformance.csv')
a = np.arange(0,1000)
df ['Columna de Arreglo'] = a
print(df)




#df['Nueva Columna']=70

```
```python
import pandas as pd 
import numpy as np
df = pd.read_csv('StudentsPerformance.csv')
a = np.random.randint(1,100, size=1000)
df ['Columna de Arreglo'] = a
print(df)




#df['Nueva Columna']=70


```
```python
import pandas as pd 
import numpy as np
df = pd.read_csv('StudentsPerformance.csv')
a = np.random.uniform(1,100, size=1000)
df ['Columna de Arreglo'] = a
print(df)




#df['Nueva Columna']=70


```
```python
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
print(df ['math score'].sum())
print(df ['math score'].count())
print(df ['math score'].mean())
print(df ['math score'].std())
print(df ['math score'].max())
print(df ['math score'].min())
#print(df.head())
```
```python
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
print(df ['math score']+ df['reading score']+ df['writing score'])
#print(df ['math score'].count())
#print(df ['math score'].mean())
#print(df ['math score'].std())
#print(df ['math score'].max())
#print(df ['math score'].min())
#print(df.head())
```
# 
**Fecha:**  21/04 

---

## 📌 Actividad 1 del Día  
### Filtros, sort_values, ascendent
```python
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
print(df[df['gender'] == 'male'].count())


print(df[df['parental level of education'] == 'high school'].sort_values(by='math score').head())

```
# 
**Fecha:**  28/04 

---

## 📌 Actividad 1 del Día  
### Obtener a los 5 usuarios más viejos de Alemania
```python
import pandas as pd
df = pd.read_csv('users.csv')
print(df[df['pais'] == 'Germany'].sort_values('edad', ascending=False).head(5))
```
## 📌 Actividad 2 del Día  
###  Obtener todos los usuarios entre las edades de 40 y 50 años 
```python
import pandas as pd
df = pd.read_csv('users.csv')
print(df['edad'].between(40, 50))
```
## 📌 Actividad 3 del Día  
###  Obtener todos los usuarios mayores de 30 años de los países Canadá, Alemania y Francia
```python
import pandas as pd
df = pd.read_csv('users.csv')
print(df[(df['pais'] == 'Canada') | (df['pais'] == 'Germany') | (df['pais'] == 'France') & (df['edad'] > 30)])
```
## 📌 Actividad 4 del Día  
###  Obtener todos los usuarios mayores de 30 años de los países Canadá.
```python
import pandas as pd
df = pd.read_csv('users.csv')
print(df[(df['pais'] == 'Canada') & (df['edad'] > 30)])
```
## 📌 Actividad 5 del Día  
###  Mostrar en consola la cantidad de hombres y mujeres. tambien el nombre y cantidad del pais que mas mujeres tiene.
```python
import pandas as pd
df = pd.read_csv('users.csv')
conteo_genero = df['genero'].value_counts()
print(conteo_genero)
mujeres = df[df['genero'] == 'female']
mujeres_por_pais = mujeres['pais'].value_counts()
pais_con_mas_mujeres = mujeres_por_pais.idxmax()
print(pais_con_mas_mujeres, mujeres_por_pais.max())

```
# 
**Fecha:**  12/05 

---

## 📌 Actividad 1 del Día
```python
import numpy as np

datos = np.array([10, 20, 30, 40, 50])

media = np.mean(datos)
std = np.std(datos, ddof=1)    
varianza = np.var(datos, ddof=1)
mediana = np.median(datos)

print("Media:", media)
print("Desviación estándar (ddof=1):", std)
print("Varianza (ddof=1):", varianza)
print("Mediana:", mediana)
```
## 📌 Actividad 2 del Día
### Obtener a los 5 usuarios mas jovenes de francia, obtener los 5 usuarios mas jovenes de australia
```python
import pandas as pd
df = pd.read_csv('users.csv')
francia_jovenes = df[df['pais'] == 'France'].sort_values('edad').head(5)
australia_jovenes = df[df['pais'] == 'Australia'].sort_values('edad').head(5)
print("5 usuarios más jóvenes de Francia:")
print(francia_jovenes)
print("\n5 usuarios más jóvenes de Australia:")
print(australia_jovenes)
```
## 📌 Actividad 3 del Día
### oBTE NER LA CANTIDAD DE PERSONAS QUE HAY EN ESPAÑA Y CUANTOS SON MASCULINOS Y CUANTOS SON FEMENINOS, HACER UN GRAFICO CON matplotlib
```python
import pandas as pd
df = pd.read_csv('users.csv')
import matplotlib.pyplot as plt

espana = df[df['pais'] == 'Spain']
total_espana = len(espana)
masculinos = len(espana[espana['genero'] == 'male'])
femeninos = len(espana[espana['genero'] == 'female'])

print(f"Total en España: {total_espana}")
print(f"Masculinos: {masculinos}")
print(f"Femeninos: {femeninos}")

plt.bar(['Masculinos', 'Femeninos'], [masculinos, femeninos], color=['blue', 'pink'])
plt.title('Cantidad de personas en España por género')
plt.ylabel('Cantidad')
plt.show()
```
# 
**Fecha:**  13/05 

---

## 📌 Actividad 1 del Día
### Obtener el nombre de todos los usuarios mayores a 50 años, dividir entre masculino y fememenino.
```python
import pandas as pd
df = pd.read_csv('users.csv')
mayores_50 = df[df['edad'] > 50]
masculinos = mayores_50[mayores_50['genero'] == 'male']['nombre']
femeninos = mayores_50[mayores_50['genero'] == 'female']['nombre']
masculinos1 = len(masculinos)
femeninos1 = len(femeninos)
print("Total de personas mayores a 50 años:\n", masculinos1 + femeninos1 )
print("Masculinos mayores de 50 años:\n", masculinos)
print("Femeninos mayores de 50 años:\n", femeninos)
import matplotlib.pyplot as plt

labels = ['Masculinos', 'Femeninos']
counts = [masculinos1, femeninos1]

plt.bar(labels, counts, color=['blue', 'pink'])
plt.title('Personas mayores de 50 años por género')
plt.ylabel('Cantidad')
plt.show()
```
## 📌 Actividad 2 del Día
### Obtener a los 20 usuarios mas viejos ed reino unido, dividir en femenino y masculino
```python
import pandas as pd
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
# Graficar edades por género
plt.bar(hombres["nombre"], hombres["edad"], label="Hombres", color="blue")
plt.bar(mujeres["nombre"], mujeres["edad"], label="Mujeres", color="pink")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.title("Top 20 usuarios más viejos del Reino Unido por género")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()
```
