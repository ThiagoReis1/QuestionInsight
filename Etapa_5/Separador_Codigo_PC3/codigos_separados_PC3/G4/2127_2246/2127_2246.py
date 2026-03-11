from numpy import*
nota= array(eval(input("nota:")))
mf= ((nota[0]+ nota[1] + nota[2] + nota[3])- min(nota))/(3.0)
print(round(mf,2))
if(mf>=50.0):
	print("APROVADO")
else:
	print("REPROVADO")