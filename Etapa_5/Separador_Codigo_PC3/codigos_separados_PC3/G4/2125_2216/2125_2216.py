from numpy import *
nt= array(eval(input("notas:")))
nf=((nt[0]*3)+(nt[1]*3)+(nt[2]*4))/10
print(round(nf,2))
if(nf<=5):
	print("REPROVADO")
else:
	print("APROVADO")