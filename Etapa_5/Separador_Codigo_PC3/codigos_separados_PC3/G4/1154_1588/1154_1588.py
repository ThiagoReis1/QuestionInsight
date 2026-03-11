#Universidade Federal do Amazonas
#Fernanda Bonfim - 21602340

n = int(input("Numero de copias: "))
taxas = float(input("Digite a taxa: "))
c = int(input("Copias por semana: "))

soma = n 
i = 0
t = taxas/100
r = 1000000

while(soma <= r):
	soma = soma - (soma * t)
	cop = soma + c
	soma = cop
	i = i + 1
print(i)