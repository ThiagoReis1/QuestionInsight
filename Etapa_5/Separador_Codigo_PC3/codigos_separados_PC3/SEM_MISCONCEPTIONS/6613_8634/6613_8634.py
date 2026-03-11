# faça seu código aqui!
N = int(input("Numero positivo: "))
numeros = 1
soma = 0
while numeros <= N:
	soma = soma + numeros**3
	numeros += 1
print("soma= ", soma)