from numpy import*

v=array(eval(input("")))
m=array(eval(input("")))

i=0
valor1=0
valor2=0
valor3=0

while(i<size(v)):
	if(m[i]=="QUENTE"):
		valor1=valor1+(90*v[i])*0.005
		
	if(m[i]=="MORNO"):
		valor2=valor2+(45*v[i])*0.005
		
	if(m[i]=="FRIO"):
		valor3=valor3

	vt=valor1+valor2+valor3
	i=i+1
print(round(vt,2))