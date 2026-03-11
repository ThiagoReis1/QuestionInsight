notaa=(float(input("digite a nota1: ")))
notab=(float(input("digite a nota 2: ")))
notac=(float(input("digite a nota 3: ")))
notafinal= (notaa + notab + notac) /3
print(round(notafinal,1))
if (notafinal >= 7):
	print("Aprovado")
else:
	print("Reprovado")
