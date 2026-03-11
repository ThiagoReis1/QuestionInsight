numero = int(input(" Digite o numero: "))
numero1 = int(input(" Digite o numero: "))
numero2 = int(input(" Digite o numero: "))
numero3 = int(input(" Digite o numero: "))

formula1 = numero1 ** 3
formula2 = numero2 ** 3
formula3 = numero3 ** 3

if formula1 + formula2 + formula3 == numero:
	print( numero, " atende a propriedade")
else:
	print( formula1 + formula2 + formula3)