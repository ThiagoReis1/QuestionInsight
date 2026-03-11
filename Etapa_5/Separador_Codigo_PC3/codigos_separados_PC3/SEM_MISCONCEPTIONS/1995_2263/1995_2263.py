a = input("aminoacido: ").lower()
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794
aspartato = (c*4) + (h*6) + (n) + (o*4)
cisteina = (c*3) + (h*7) + (n) + (o*2) + (s)
metionina = (c*5) + (h*11) + (n) + (o*2) + (s)
if (a == "aspartato"):
	print(round(aspartato,2))
elif (a == "cisteina"):
	print(round(cisteina,2))
elif (a == "metionina"):
	print(round(metionina,2))
else:
	print("Entrada:", a)
	print("Dado Invalido")