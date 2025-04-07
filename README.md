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
#FUNCIONES   
# .head() - muestra las primeras 5 filas    
# .tail() - muestra las ultimas 5 filas   
# .describe() - muestra estadisticas de las columnas numericas   
# .info() - muestra las filas vacias (Tipo de data de nada es: non-null)  
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

