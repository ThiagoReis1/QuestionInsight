aminoacido = input("nome do aminoacido: ").lower()

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

aspartato = 4*c + 6*h + 1*n + 4*o
cisteina = 3*c + 7*h + 1*n + 2*o + 1*s
metionina = 5*c + 11*h + 1*n + 2*o + 1*s

if (aminoacido == "aspartato"):
	print(round(aspartato,2))
	
elif (aminoacido == "cisteina"):
	print(round(cisteina,2))
	
elif (aminoacido == "metionina"):
	print(round(metionina,2))
	
else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")