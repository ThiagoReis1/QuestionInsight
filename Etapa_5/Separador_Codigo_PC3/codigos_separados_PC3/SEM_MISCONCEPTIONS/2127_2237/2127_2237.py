from numpy import *
notas=array(eval(input("aaaa : ")))
MFinal=(sum(notas)-min(notas))/3.0

print(round(MFinal,2))
if (MFinal>=50) :
	print("APROVADO")
else:
	print("REPROVADO")




