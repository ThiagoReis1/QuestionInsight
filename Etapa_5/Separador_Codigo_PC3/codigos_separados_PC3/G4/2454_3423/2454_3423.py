a= float(input("Altura(m): "))
s= input("sexo: ")

m= (72.7*a)-58
f= (62.1*a)-44.7

if (a < 1.0) or (a > 2.5):
	print("altura invalida")
elif s == "M":
	print(round(m,2))
elif s == "F":
	print(round(f,2))
else:
	print("codigo invalido de sexo")
