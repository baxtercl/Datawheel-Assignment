import pandas as pd

filesavecsv = 'salaries.csv'

df_state = pd.read_csv('state.csv')
df = pd.read_csv('data.csv')

df_state['Code'] = df_state['Code'].astype(int)
df_state.set_index('Code', inplace=True)

salarios_maximos = df.groupby('State').max().reset_index()
salario_promedio = df.groupby('State').mean().reset_index()
salario_total = df.groupby('State').sum().reset_index()

salario_promedio = salario_promedio.rename(columns={"Salary": "Mean"})
salarios_maximos = salarios_maximos.rename(columns={"Salary": "Max"})
salario_total = salario_total.rename(columns={"Salary": "Total"})

df_final = salario_promedio.merge(salarios_maximos, on='State').merge(salario_total, on='State')
df_final.replace(to_replace=df_state['State'], inplace=True)
df_final.sort_values(by='Max', ascending=False, inplace=True)
df_final.set_index('State', inplace=True)

df_final.to_csv(filesavecsv, float_format='%.3f')

print(df_final)