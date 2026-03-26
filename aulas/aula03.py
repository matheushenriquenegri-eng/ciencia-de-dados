import matplotlib.pyplot as plt

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','junho']
vendas = [200, 300, 340, 305, 360, 400]

plt.plot(meses, vendas, color='blue')
plt.title("Vendas no Primeiro Semestre")

plt.xlabel('Meses')
plt.ylabel('Vendas')

plt.show()
plt.savefig('aula03')