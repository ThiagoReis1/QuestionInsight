from numpy import *

notas = array(eval(input("Digite as notas: ")))
mf = (sum(notas)-max(notas))/3.0

if(mf >= 50.0):
	print(round(mf,2))
	print("APROVADO")
else:
	print(round(mf,2))
	print("REPROVADO")

