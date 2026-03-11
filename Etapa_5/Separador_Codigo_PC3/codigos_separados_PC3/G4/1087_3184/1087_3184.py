a = float(input("primeira nota"))
b = float(input("segunda nota"))
c = float(input("terceira nota"))
d = float(input("quarta nota"))

m = (a+b+c+d)/4

if(m<7):
	print(round(m , 2))
	print("Reprovado")
else:
	print(round(m , 2))
	print("Aprovado")
