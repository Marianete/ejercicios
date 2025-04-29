import pandas as pd
df = pd.read_csv('users.csv')
##germany_data = df[df['pais'] == 'Germany'].sort_values('edad', ascending=False)
##top_5 = germany_data.head(5)
##media_edad = top_5['edad'].mean()
##print(df['edad'].between(40, 50))
##print(df[(df['pais'] == 'Canada') | (df['pais'] == 'Germany') | (df['pais'] == 'France') & (df['edad'] > 30)])
conteo_genero = df['genero'].value_counts()
print(conteo_genero)
mujeres = df[df['genero'] == 'female']
mujeres_por_pais = mujeres['pais'].value_counts()
pais_con_mas_mujeres = mujeres_por_pais.idxmax()
print(pais_con_mas_mujeres, mujeres_por_pais.max())

