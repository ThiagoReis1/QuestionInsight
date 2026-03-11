a = input("Digite 'T' para tapioca ou 'S' para salgados: ").upper()
b = int(input("A quantidade de tapiocas ou salgados: "))
c = int(input("A quantidade de acais: "))

if a == "T":
	valor = 5.5*b + c*10
	print(round(valor,2))
else: 
	valor = 4*b + c*10
	print(round(valor,2))