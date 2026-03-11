from numpy import *
n=array(eval(input("informe as notas:")))

nf=(n[0]*2.0+n[1]*3.0+n[2]*5.0)/10.0

print(nf)

if(nf>=(5.0)):
	msn="APROVADO"
else:
	msn="REPROVADO"
print(msn)

	




