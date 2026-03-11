from numpy import*
m=98.48
dist = array(eval(input("digite um numero :")))
i=0
x=0
while(i<size(dist)):
	if(dist[i]>m):
		x=x+1
	i+=1
print(m)
print(x)