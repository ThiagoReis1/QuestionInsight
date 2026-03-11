from numpy import*
vet= array(eval(input("Notas:")))

mf=(vet[0]*1.0 + vet[1]*2.0 +vet[2]*3.0 + vet[3]*4.0)/(10.0)
print(round(mf,2))

if (mf >= 5) :
	print("APROVADO")
else:
	print("REPROVADO")
