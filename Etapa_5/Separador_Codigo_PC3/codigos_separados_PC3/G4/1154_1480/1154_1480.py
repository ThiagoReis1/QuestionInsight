#Universidade Federal do Amazonas
#Exerc. Avaliativo Olímpico
#Pedro Vinícius Borges de Souza - 21650221
#Engenharia Química

n = int(input("Copias: "))
taxa = float(input("Taxa: "))
c = int(input("Copias por semana: "))

soma = n
i = 0
t = taxa/100
r = 1000000

while (soma <= r):
	soma = soma - (soma * t)
	cop = soma + c
	soma = cop
	i = i + 1
print(i)