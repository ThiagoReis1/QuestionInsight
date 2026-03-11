clientes = input("respostas dos clientes (S, I, N): ").upper()
soma =  0
cont = 0
while (clientes != "X"):
	if (clientes == "S"):
		soma = soma + 1
	
	clientes = input(": ")
print(soma)
