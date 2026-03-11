# faça seu código aqui!

n = int(input())

contador = 1
soma = 0

while contador <= n:
	soma += contador ** 3
	contador += 1
	
print("soma= {}".format(soma))