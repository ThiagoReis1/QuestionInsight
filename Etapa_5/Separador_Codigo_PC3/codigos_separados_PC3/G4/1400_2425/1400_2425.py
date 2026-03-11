a = input("Tipo de ataque:")
b = int(input("Número de rodadas:"))
c = int(input("Valor 1:"))
d = int(input("Valor 2:"))

if(a == "constricao"):
	N = c + d + 1
	p = b*N
	print(p)
if(a == "polen"):
	R = c*d
	print(R)