nota = float(input("Qual a nota: "))
if(nota > 10) or (nota < 0):
	print("ERRO")
	
else:
	if(nota >= 10):
		print("A")
	elif(nota >= 8):
		print("B")
	elif(nota >= 7):
		print("C")
	elif(nota >= 6):
		print("D")
	elif(nota >= 4):
		print("E")
	elif(nota < 4):
		print("F")

