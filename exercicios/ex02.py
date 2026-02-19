import matplotlib.pyplot as plt

#construa um gráfico de barras que compare os celulares mais vendidos em 2026
celulares = ['iPhone 17 Pro Max ','iPhone 17','Xiaomi 17']
faturamento = [200000, 320000, 500000]

plt.bar(celulares,faturamento)
plt.show()
plt.savefig('./exercicios/ex02.png')