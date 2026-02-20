import matplotlib.pyplot as plt

# 3) Identifique na turma qual é o time de cada um e contrua um gráfico de barras para mostrar a popularidade  cada time
times = ['Grêmio ','Flamengo','Palmeiras','Internacional','Vasco']
torcedores = [3, 2, 1, 2, 1]
cores = ['#0D80BF','#C52613','#006437','#E5050F','#000000']

plt.bar(times,torcedores,color=cores)
plt.xlabel('Times do campeonato brasileiro')
plt.ylabel('N°  de torcedores')
plt.show()
plt.savefig('./exercicios/ex03.png')