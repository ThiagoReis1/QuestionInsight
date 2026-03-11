numero = int(input("qual o valor do número"))
formula = (numero//100 + numero%100)**2
if numero == formula:	
	print("X atende a propriedade")
else:
	print("formula")