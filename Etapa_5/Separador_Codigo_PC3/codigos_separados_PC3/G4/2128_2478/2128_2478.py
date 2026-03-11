from numpy import *
v = array(eval(input("Informe as notas: ")))
a = max(v)
b = sum(v)
mf = (b-a)/3 
if(mf < 50):
	print(round(mf, 2))
	print("REPROVADO")
if(mf>=50):
	print(round(mf, 2))
	print("APROVADO")