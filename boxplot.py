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
plt.show()
sns.swarmplot(df_result, x="algoritmo", y = 'fitness')
plt.show()
