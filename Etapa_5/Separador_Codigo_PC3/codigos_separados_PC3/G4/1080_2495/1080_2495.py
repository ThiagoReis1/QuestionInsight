n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
m = (n1+n2+n3)/3
if(m>=5):
	print(round(m,1))
	print("Aprovado")
else:
	print(round(m,1))
	print("Reprovado")