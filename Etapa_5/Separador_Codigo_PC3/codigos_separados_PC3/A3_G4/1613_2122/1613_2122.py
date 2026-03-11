from numpy import*
v = array(eval(input().upper()))
vet = array(eval(input()))
i = 0
c = 0
b = 0
g = 0
d = 0
l = 0
while(i<size(v)):
	if(v[i] == "ALONGAMENTO"):
		c = vet[i]*3.0
	if(v[i] == "CORRIDA"):
		b =vet[i]*10.3
	if(v[i] == "DANCA"):
		g = vet[i]*6.7
	if(v[i] == "ESCALADA"):
		d = vet[i]*9.7
	if(v[i]== "HIDROGINASTICA"):
		l = vet[i]*5.0
	i=i+1	
print(round(c+b+d+g+l,2))
		
	
	


