from numpy import*

nota = array(eval(input("Notas dps alunos:")))


mfinal = (nota[0]*1.0 + nota[1]*2.0 + nota[2]*3.0 + nota[3]*4.0)/10.0

print(round(mfinal,2))

if(mfinal >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")