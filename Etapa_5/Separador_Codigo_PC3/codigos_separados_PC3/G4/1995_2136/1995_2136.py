am = input("nome do aminoacido: ").lower()

#dados
o=15.9994
c=12.011
n=14.0067
s=32.066
h=1.00794

if(am=="aspartato"):
	pm = 4*c + 6*h + n + 4*o
	print(round(pm,2))
elif(am=="cisteina"):
	pm = 3*c + 7*h + n + 2*o + s
	print(round(pm,2))
elif(am=="metionina"):
	pm = (5*c +11*h + n + 2*o + s)
	print(round(pm,2))
else:
	print("Entrada: ", am)
	print("Dado Invalido")