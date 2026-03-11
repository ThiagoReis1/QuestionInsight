from numpy import*
v=array(eval(input("Custo de itens: ")))
i=0
d=0
s=0
while(i < size(v)):
	if(v[i]> 80):
		d=d+(v[i]-5)
	elif(v[i]<=80):
		s=s+v[i]
		i=i+1
print(round(d+s,2))
	
	
