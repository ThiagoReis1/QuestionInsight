from numpy import *
t=array(eval(input("informe os tempos:")))
m=array(eval(input("informe os modos:")))

i=0

q=90
m=45
f=0

while(i<size(m)):
	if(str(m[i])=="QUENTE"):
		ct=q*t[i]*q*0.005
	elif(str(m[i])=="MORNO"):
		ct=m*t[i]*m*0.005
	elif(str(m[i])=="FRIO"):
		ct=f*t[i]*f*0.005
	soma=soma+ct
	i=i+1
print(round(soma,2))
	
