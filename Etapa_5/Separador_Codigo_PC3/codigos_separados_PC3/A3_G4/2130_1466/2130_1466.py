from numpy import *
a=array(eval(input()))
i=0
s=(a[0]*3+a[1]*2+a[2]*2+a[3]*3)/10
print(round(s,2))
if(s>=5):
	print("APROVADO")
else:
	print("REPROVADO")