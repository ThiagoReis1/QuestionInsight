from numpy import*

vet=array(eval(input("digite as notas: ")))
med=(sum(vet)-min(vet))/3

print(round(med,2))
if(med>=50.0):
	print("APROVADO")
else:
	print("REPROVADO")