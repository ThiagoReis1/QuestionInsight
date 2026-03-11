a = input("poder polen ou contricao: ")
n = int(input("numero de rodadas: "))
v1 = int(input("valor 1: "))
v2 = int(input("valor 2: "))

if(a == "polen"):
	x = v1*v2
else:
	x = (v1+v2)+1
print(x)