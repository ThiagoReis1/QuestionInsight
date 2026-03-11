varA = input("digite 'T' para tapioca e 'S' para salgado: ")
varB = float(input("digite a quantidade de tapiocas ou salgados: "))
varC = float(input("digite a quantidade de acais: "))

if varA == 'T':
	varX = (varB * 4.50) + (varC * 12.00)
	print(round(varX , 2))
	
else:
	varX = (varB * 5.00) + (varC * 12.00)
	print(round(varX , 2))