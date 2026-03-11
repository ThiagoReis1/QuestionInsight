nota01 = float(input("informe a nota 1:  "))
nota02 = float(input("informe a nota 2:  "))
nota03 = float(input("informe a nota 3:  "))

media = (nota01 + nota02 + nota03) /3

if (media>=5.0):
	print(round(media,1))
	print("Aprovado")
	
else:
	print(round(media,1))
	print("Reprovado")
	
	
