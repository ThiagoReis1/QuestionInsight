numint = int(input("Qual o numero?"))

if numint % 29 == 0:
	print(numint // 29)
	print("sim")
else:
	print(numint % 29)
	print("nao")
