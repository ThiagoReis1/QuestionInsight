from numpy import*
v = array(eval(input("tempo de chegada: ")))

var = min(v)
i = 0
p =0

while(i<size(v)):
	
	if(v[i]== var):
		p = i
	i = i  +1	
print(p)