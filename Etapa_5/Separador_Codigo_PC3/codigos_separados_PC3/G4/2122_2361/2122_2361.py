from numpy import *
n = array(eval(input("Digite as Notas Parciais: ")))
mf = ((n[0]*2.0) + (n[1]*3.0) + (n[2]*5.0)) / 10.0
print(round(mf, 2))
if (mf >= 5.0):
	print ("APROVADO")
else:
	print ("REPROVADO")