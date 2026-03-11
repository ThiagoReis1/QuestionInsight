n1 = float(input("digite a nota"))
n2 = float(input("digite a nota"))
n3 = float(input("digite a nota"))
n4 = float(input("digite a nota"))
n5 = float(input("digite a nota"))

med = (n1 + n2 + n3 + n4 + n5)/5

if (med >= 6):
	print(round(med,2))
	print("Aprovacao")
else:
	print(round(med,2))
	print("Reprovacao")