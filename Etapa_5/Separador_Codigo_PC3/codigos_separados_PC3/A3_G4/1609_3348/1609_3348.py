from numpy import*
v= array(eval(input()))
print(v[1])
u= input()
i=0
j=0

while(i<size(v)):
	n= v[i].replace("L","R")
	if(u==v[i]):
		j = i
	if(u!=v[i]):
		j = "NAO ENCONTRADA"
	i= i + 1
print(j)
