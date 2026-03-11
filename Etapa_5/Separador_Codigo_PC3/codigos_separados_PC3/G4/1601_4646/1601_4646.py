from numpy import*
v= array(eval(input("tempo dos corredores")))
i = 0
while(i<size(v) and v[i]!=min(v)):
	i+=1
print(i)