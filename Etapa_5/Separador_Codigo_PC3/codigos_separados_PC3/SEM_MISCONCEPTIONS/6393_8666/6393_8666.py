mensagem = [int(,) for ,  in input(,)]

def transforma_numero(numero):
	if numero == 0:
		return 0
	else:
		return (numero + 1) ** 3
	
mensagem_transformada = transforma_numero(numero)

print(mensagem_transformada)