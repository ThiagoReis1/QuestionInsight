nota = float(input("Digite a nota: "))

if (nota < 0) or (nota > 10):
	print ("ERRO")
elif (nota >= 0) and (nota < 5.0):
	print ("F")
elif (nota >= 9.0) and (nota <= 10):
	print ("A")
elif (nota >= 8.0) and (nota < 9.0):
	print ("B")
elif (nota >= 7.0) and (nota < 8.0):
	print ("C")
elif (nota >= 6.0) and (nota < 7.0):
	print ("D")
elif (nota >= 5.0) and (nota < 6.0):
	print ("E")