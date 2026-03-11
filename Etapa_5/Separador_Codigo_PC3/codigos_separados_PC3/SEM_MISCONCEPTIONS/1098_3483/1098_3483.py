numero = int(input("Digite o numero: "))

parte_a = numero//1000
parte_b = numero % 1000

calculo=(parte_a - parte_b)**4
if calculo == numero:
	mensagem="atende"
else:
	mensagem="nao atende"
	
print(numero,mensagem)


 

