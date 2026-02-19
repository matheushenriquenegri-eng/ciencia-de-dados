import matplotlib.pyplot as plt

# Exercício - construa um gráfico de barras que compare a nota de popularidade de séries em 2025
series = ['Stranger Things ','It','Game of Thrones','Friends']
notas = [5.0, 5.0, 4.8, 3.5]

plt.bar(series,notas)
plt.show()
plt.savefig('./exercicios/ex01.png')