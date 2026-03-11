from numpy import*
vet = array(eval(input("")))
p = vet[0]*5
s = vet[1]*3
t = vet[2]*2
nota = (p + s + t)/10
print(round(nota,2))
if(nota >= 5):
	print("APROVADO")
else:
	print("REPROVADO")