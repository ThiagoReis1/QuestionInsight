a = float(input("notas: "))
b = float(input("notas: "))
c = float(input("notas: "))

m = (a+b+c)/3

if m >=5 :
	print(round(m,1))
	print("Aprovado")
else:
	print(round(m,1))
	print("Reprovado")
