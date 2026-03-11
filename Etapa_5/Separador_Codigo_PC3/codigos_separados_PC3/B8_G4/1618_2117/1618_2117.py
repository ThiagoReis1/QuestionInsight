from numpy import*
v=array(eval(input("digite os coeficientes: ")))

a=size(v)-1
i=0
saida=""

while(a>=0):
	if(a==1):
		saida=saida+(str(v[i]))+"x"+" + "
	elif(a==0):
		saida=saida+(str(v[i]))
	if(a>1):
		saida=saida+(str(v[i])+"x^"+str(a)+" + ")
	i=i+1
	a=a-1
print(saida)