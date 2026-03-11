numero = int(input("Qual o numero?: "))
numero1 = numero//1000
resto_numero1 = numero%1000

formula  = (numero1 + resto_numero1)**2  
if numero == formula:
	print("atende")
	print(numero)
else:
	print("nao atende")
	print(numero)
	
	