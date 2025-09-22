import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

results = np.loadtxt("resultados.txt")
resultados = results.tolist()

algoritmo  = ['Hill Climbing'] * len(resultados)

df_result = pd.DataFrame({'fitness': resultados, 'algoritmo' : algoritmo})

sns.boxplot(df_result, x="algoritmo", y = 'fitness')

sns.boxplot(df_result, x="algoritmo", y = 'fitness')
sns.swarmplot(df_result, x="algoritmo", y = 'fitness')
# plt.show()


### Analisando 2 algoritmos (agora com estocastico)

results_2 = np.loadtxt("resultados_estocastico.txt")
resultados_2 = results_2.tolist()
algoritmo2 = ['Hill Climbing Estocástico'] * len(resultados_2)

df_result2 = pd.DataFrame({'fitness': resultados_2, 'algoritmo' : algoritmo2})

df_final = pd.concat([df_result, df_result2])

df_final = df_final.reset_index(drop=True)

sns.boxplot(df_final, x="algoritmo", y = 'fitness', hue = "algoritmo")
sns.swarmplot(df_final, x="algoritmo", y = 'fitness', hue = "algoritmo")
plt.show()