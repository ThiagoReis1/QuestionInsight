n1 = float(input("insira a nota 1 "))
n2 = float(input("insira a nota 2 "))
n3 = float(input("insira a nota 3 "))
n4 = float(input("insira a nota 4 "))
n5 = float(input("insira a nota 5 "))

media = ((n1+n2+n3+n4+n5)/5)

print(n1, n2, n3, n4, n5)

if (media >= 6): 
	print(round(media, 2.0))
	print("aprovado")	
else:
	print(round(media, 2.0))
	print("reprovado")	