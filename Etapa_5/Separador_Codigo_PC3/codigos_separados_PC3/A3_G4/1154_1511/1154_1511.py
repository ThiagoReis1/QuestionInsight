n = int(input("Digite o numero de copias: "))
taxa = float(input("Taxas: "))
c = int( input("Copias por semana: "))

soma = n
i = 0
t = taxa/100
r = 1000000

while (soma <= r):
	soma = soma + (soma * t)
	cop = soma + c
	i = i + 1
print(i)