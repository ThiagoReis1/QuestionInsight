from numpy import* 
v = array(eval(input("Temperatura:")))
i = 0
cont = 0
while (i<size(v)):
	if(v[i]>=-100):
		cont= cont+1
	i = i+ 1 
p=array(zeros(cont,dtype = float))
i = 0 
k = 0
while(i<size(v)):
	if(-100 <= v[i]):
		p[k]= v[i]
		k = k+1
	i = i+1
print(p)
	