from numpy import*

v=array(input(":"))
tempo=array(eval(input(":")))

alongamento=3.0
corrida=10.3
danca=6.7
escalada=9.7
hidroginastica=5.0
i=0
x = 0
while(i<size(tempo)):
	if(v[i]=="ALONGAMENTO"):
		x= x + alongamento*tempo[i]
	if(v[i]=="CORRIDA"):
		x= x + corrida*tempo[i]
	if(v[i]=="DANCA"):
		x= x + danca*tempo[i]
	if(v[i]=="ESCALADA"):
		x= x + escalada*tempo[i]
	if(v[i]=="HIDROGINASTICA"):
		x= x + hidroginastica*tempo[i]
	i=i+1
print(x)		