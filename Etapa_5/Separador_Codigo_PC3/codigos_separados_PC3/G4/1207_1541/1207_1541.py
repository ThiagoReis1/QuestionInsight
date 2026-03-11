from numpy import*

v= array(eval(input("distancia:")))
i = 0
k = 0
recorde = 98.48
while(i < size(v)):
	if(v[i]>recorde):
		k = k + 1
	i = i + 1

print(recorde)
print(k)

				 