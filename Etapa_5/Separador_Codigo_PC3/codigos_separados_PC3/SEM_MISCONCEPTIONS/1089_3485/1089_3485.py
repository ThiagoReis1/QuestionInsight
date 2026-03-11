n1 = float(input("Valor"))
n2 = float(input("Valor"))
n3 = float(input("Valor"))

limite = float(input("Limite"))
v = n1+n2+n3
print(v)

if (v <= limite):
	mensagem = "Nao ultrapassou"
else:
	mensagem = "Ultrapassou"
	
print(mensagem)