from numpy import*
c=array(eval(input("Custo dos itens:")))
f=size(c)
t=0
i=0
while(i<f):
	t=t+c[i]
	if(c[i]>80.00):
		t=t-5.00
	i=i+1
		
print(round((float(t)),2))
