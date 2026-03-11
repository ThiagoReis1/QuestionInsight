from numpy import *
nota1 = array(eval(input("notas parciais de um aluno: ")))


mf = (sum(nota1) - min(nota1))/3
if(mf >= 5):
	print(float(round(mf,2)))
	print("APROVOU")
else:
	print(float(round(mf,2)))
	print("REPROVOU")
	



