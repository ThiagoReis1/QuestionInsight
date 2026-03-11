#TAMBAQUI
qtd = int(input("Digite a quantidade inicial de tambaquis"))
i = float(input("Digite a taxa anual de crescimento dos peixes:"))
retirados = int(input("Digite a quantidade de tambaqui retirado por ano"))
x = 1
while (qtd > 0):
   	qtd = qtd + ((qtd * i) - retirados)
   	x = x + 1
print (x)