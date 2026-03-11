numero = int(input("Qual o numero? "))
formula = (numero//132 + numero%496)**2


if numero == formula:
	print("X atende propriedade")
else:
   print("X nao atende a propriedade")