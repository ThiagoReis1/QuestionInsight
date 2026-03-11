from numpy import *

v=array(eval(input("Digite o numero real positivo: ")))

i=0
while(i<0):
m=(((v[i]*v[i-1]**5)/i)**1/5))
i+=1
print(round(m, 2))
	

