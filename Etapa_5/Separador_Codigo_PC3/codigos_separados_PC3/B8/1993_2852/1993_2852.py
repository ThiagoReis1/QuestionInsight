am = input(" aminoacido ").lower()
#atomos
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794
#aminoacidos
cisteina = 3*c + 7*h + n + 2*o + s
isoleucina = 6*c +13*h + n + 2*o
metionina = 5*c + 11*h + n + 2*o + s

if (am == "cisteina" or am == "isoleucina" or am == "metionina"):
	if(am == "cisteina"):
	   print(round(cisteina,2))
	elif (am == "isoleucina"):
		print(round(isoleucina,2))
	elif (am == "metionina"):
		print(round(metionina,2))
else :
	print("Entrada:", am)
	print("Dado Invalido")