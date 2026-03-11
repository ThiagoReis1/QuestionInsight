a = input("nome do aminoacido: ")

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

if(a.lower() == "aspartato"):
	p = (4*c + 6*h + n + 4*o)
	print(round(p,2))
elif(a.lower() == "cisteina"):
	p = (3*c + 7*h + n + 2*o + s)
	print(round(p,2))
elif(a.lower() == "metionina"):
	p = (5*c + 11*h + n + 2*o + s)
	print(round(p,2))
else:
	print("Entrada:", a)
	print("Dado Invalido")