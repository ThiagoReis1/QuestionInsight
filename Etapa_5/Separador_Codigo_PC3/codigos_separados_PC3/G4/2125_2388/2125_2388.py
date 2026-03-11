
from numpy import*
nt= array(eval(input("notas: ")))

f= (nt[0]*3 + nt[1]*3 + nt[2]*4) / 10
print(round(f,2))

if(f > 5.0):
	print('APROVADO')
else:
	print('REPROVADO')