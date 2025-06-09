
# Python 

##  Pandas

### Atributos Principales  
- **.dtypes**: Tipo de datos de cada columna.  
- **.shape**: Tupla (filas, columnas) del DataFrame.  
- **.mean**: Media de columnas numéricas.  
- **.min**: Valor mínimo de columnas numéricas.  
- **.max**: Valor máximo de columnas numéricas.  
- **.county**: Cantidad de valores no nulos por columna.  

### Funciones Clave  
- **.head(n)**: Primeras n filas (default: 5).  
- **.tail(n)**: Últimas n filas (default: 5).  
- **.describe()**: Estadísticas descriptivas (media, std, min, max, percentiles).  
- **.info()**: Resumen del DataFrame (tipos de datos, valores no nulos).  
- **.to_*()**: Conversión de formatos:  
  - .to_csv(): Guarda a CSV.  
  - .to_excel(): Guarda a Excel.  
- **.iloc[]**: Acceso por índice numérico:  
  - Ej: .iloc[:, -3]: Últimas 3 columnas.  
### Actividades 
1. Actividad 1: Obtener todos los usuarios mayores de 30 años de los países Canadá, Alemania y Francia.[Respuesta](https://github.com/Marianete/ejercicios?tab=readme-ov-file#-actividad-3-del-d%C3%ADa)
2. Actividad 2: Obtener todos los usuarios mayores de 30 años de los países Canadá. [Respuesta](https://github.com/Marianete/ejercicios?tab=readme-ov-file#-actividad-4-del-d%C3%ADa)


---

##  Matplotlib

### Componentes Principales  
1. **pyplot**: Módulo principal para gráficos.  
   - Ej: import matplotlib.pyplot as plt.  
2. **Figura y Ejes**:  
   - plt.figure(): Crea una figura.  
   - plt.subplots(): Crea ejes (axes).  
3. **Tipos de Gráficos**:  
   - Línea: plt.plot().  
   - Barras: plt.bar().  
   - Dispersión: plt.scatter().  
   - Histograma: plt.hist().  
4. **Personalización**:  
   - Títulos: plt.title(), plt.xlabel(), plt.ylabel().  
   - Leyendas: plt.legend().  
   - Grid: plt.grid(True).  
5. **Guardar Gráficos**:  
   - plt.savefig('nombre.png').  


### Flujo Básico  
1. Crear figura/ejes → 2. Generar gráfico → 3. Personalizar → 4. Mostrar/Guardar.  
### Actividades 
1. Actividad 1: Grafica la temperatura promedio de lunes a viernes (°C).  
    - [Codigo resolucion en GitHub](https://github.com/Marianete/ejercicios/blob/main/matploib1.py)
      - [Imagen del grafico obtenido](https://github.com/Marianete/ejercicios/blob/main/Figure_1.png)
#  IA & ML - Mapa Conceptual

##  **Inteligencia Artificial (IA)**  
- **Definición:** Sistemas que realizan tareas inteligentes  
- **Tipos:**  
    - *IA Débil*  
        - Tareas específicas  
        - Ej: Siri, Netflix  
    - *IA General (AGI)*  
        - Teórica (no existe aún)  
    - *Superinteligencia (ASI)*  
        - Hipotética  
- **Aplicaciones:**  
  - Diagnóstico médico  
  - Coches autónomos  
  - Traducción automática  
---

## **Machine Learning (ML)**  
- **Definición:** Algoritmos que aprenden de datos  
- **Tipos:**  
  - *Supervisado*  
    - Datos etiquetados  
    - Ej: Precios inmuebles, spam  
  - *No Supervisado*  
    - Datos sin etiquetas  
    - Ej: Segmentación clientes  
  - *Por Refuerzo*  
    - Sistema de recompensas  
    - Ej: AlphaGo  
  - *Deep Learning*  
    - Redes neuronales  
    - Ej: ChatGPT, reconocimiento facial  
- **Aplicaciones:**  
  -  Recomendaciones personalizadas  
  -  Predicción de enfermedades  
  -  Mantenimiento predictivo  

---
# DataFrame vs Dataset

## DataFrame  
- **Definición**  
  Estructura de datos tabular (filas y columnas) en Python/R.  
- **Características**  
  - Columnas con nombres y tipos definidos (ej: entero, texto).  
  - Filas indexadas (numérico o personalizado).  
  - Optimizado para operaciones (filtrado, agrupación, cálculos).  
  - Almacena datos heterogéneos (diferentes tipos por columna).  
- **Ejemplos**  
  - Tablas en Pandas (Python).  
  - data.frame en R.  
- **Casos de uso**  
  - Análisis estadístico.  
  - Manipulación de datos estructurados.  

---

## Dataset  
- **Definición**  
  Colección de datos organizados (estructurados, semiestructurados o no estructurados).  
- **Características**  
  - Puede incluir múltiples formatos: tablas, texto, imágenes, etc.  
  - No requiere estructura fija.  
- **Ejemplos**  
  - Archivo CSV/Excel.  
  - Conjunto de imágenes para entrenar modelos de IA.  
  - Documentos JSON/XML.  
- **Casos de uso**  
  - Almacenamiento de datos brutos.  
  - Entrenamiento de modelos de machine learning.  

---
# Big Data: Las 5 V's (Mapa Mental)

##  **Las 5 V's**  
### **1. Volumen**  
- **Definición:** Datos masivos (TB, PB, ZB).  
- **Importancia:**  
  - Facebook: 500+ TB/día.  
  - CERN: 1 PB/segundo en experimentos.  
- **Herramientas:** Hadoop HDFS, Amazon S3, Apache Spark.  

### **2. Velocidad**  
- **Definición:** Flujo rápido de datos en tiempo real.  
- **Casos clave:**  
  - NYSE: 10M+ transacciones/día.  
  - Twitter: 350K tweets/minuto en eventos.  
- **Tecnologías:** Apache Kafka, Flink.  

### **3. Variedad**  
- **Tipos de datos:**  
  - Estructurados (SQL).  
  - No estructurados (videos, redes sociales).  
  - Semiestructurados (JSON, logs).  
- **Ejemplos:**  
  - GPS en logística (Uber).  
  - Biometría en smartphones.  

### **4. Veracidad**  
- **Desafíos:**  
  - Datos duplicados/incompletos.  
  - Sesgos en IA.  
- **Soluciones:**  
  - Limpieza: Pandas, OpenRefine.  
  - Validación: Apache NiFi.  

### **5. Valor**  
- **Impacto económico/social:**  
  - Netflix: Ahorro de $1B anuales con recomendaciones.  
  - Agricultura: +20% cosechas con IoT.  

---

##  **Aplicaciones Clave**  
- **Salud:**  
  - Diagnóstico predictivo (IBM Watson Oncology).  
- **Retail:**  
  - Personalización en tiempo real (Amazon).  
- **Energía:**  
  - Smart grids (Europa).  
- **Transporte:**  
  - Vehículos autónomos (Tesla Autopilot).  

---

##  **Futuro del Big Data**  
- **IA integrada:** ChatGPT analizando petabytes de texto.  
- **Edge Computing:** Procesamiento en drones agrícolas.  
- **Ética:** Regulaciones como GDPR.  

---

##  **Herramientas Destacadas**  
- **Almacenamiento:** Hadoop HDFS, Amazon S3.  
- **Procesamiento:** Apache Spark, Flink.  
- **Limpieza:** Pandas, OpenRefine. 


# Seaborn - Mapa Mental

## 1. Importación y Datos
- Importar Seaborn y otras bibliotecas necesarias
- Cargar datasets de ejemplo (`sns.load_dataset()`)

## 2. Tipos de Gráficos
### Dispersión
- `sns.scatterplot()`

### Histograma
- `sns.histplot()`

### Caja (Boxplot)
- `sns.boxplot()`

### Barras
- `sns.barplot()`

### Violín
- `sns.violinplot()`

## 3. Personalización
- Títulos con `plt.title()`
- Etiquetas de eje con `plt.xlabel()`, `plt.ylabel()`
## Actividades 
1. Actividad: Ejemplo de uso de la libreria: [Enlace](https://github.com/Marianete/ejercicios/blob/main/seaborn1.py)