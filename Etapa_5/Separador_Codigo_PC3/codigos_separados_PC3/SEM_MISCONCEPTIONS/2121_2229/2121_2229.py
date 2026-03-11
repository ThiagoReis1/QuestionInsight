from numpy import*
nota=array(eval(input("notas: ")))

Nfinal= (nota[0]*5.0 + nota[1]*3.0 + nota[2]*2.0)/10


print(round(Nfinal,2))
if(Nfinal>=5.0):
	print("APROVADO")
else:
	print("REPROVADO")