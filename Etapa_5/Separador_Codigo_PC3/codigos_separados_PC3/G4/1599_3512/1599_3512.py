from numpy import*

vtr= array(eval(input("Vasco eh ruim: ")))

i=0
v=0

while(i<size(vtr)):
	if(vtr[i]>80):
		v= v + vtr[i] - 0.15* vtr[i]
	else:
		v= v + vtr[i]
	i=i + 1
	
print(round(v,2))