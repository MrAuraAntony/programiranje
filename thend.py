import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
df_lokacije = pd.read_csv('mars_lokacije.csv', sep=';', decimal=',')
df_uzorci = pd.read_csv('mars_uzorci.csv', sep=';', decimal=',')
df = pd.merge(df_lokacije, df_uzorci, on='ID_Uzorka')
uvjet_anomalije = (df['Temperatura'] < -80) | (df['Temperatura'] > -30) | (df['Vlaga'] > 6)
df_anomalije = df[uvjet_anomalije]
df_cisto = df[~uvjet_anomalije]
# GRAPH 1: Temperatura i vlaga, ovisno o metanu plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cisto, x='Temperatura', y='Vlaga', hue='Metan')
plt.title('Odnos temperature i vlage')
plt.savefig('graph1_temp_h2o.png')
plt.close()
# GRAPH 2: Heatmap dubine plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='Dubina', palette='viridis', size='Dubina')
plt.title('Karta dubine bušenja')
plt.savefig('graph2_heatmap_depth.png')
plt.close()
# GRAPH 3: Očitanja metana plt.figure(figsize=(10, 6)) .