a = int(input("Quantidade de votos para Ambrosio Rutra: "))
d = int(input("Quantidade de votos para Demelza Olecram:"))
if (a>d):
	print("Ambrosio Rutra")
	print(round((a*100)/(a+d),2))
else:
	print("Demelza Olecram")
	print(round((d*100)/(a+d),2))

