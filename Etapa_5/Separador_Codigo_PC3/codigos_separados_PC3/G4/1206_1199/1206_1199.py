from numpy import *
d = array(eval(input("Digite o valor das distancias: ")))
i = 0 
recorde = 8.95
s = 0 

while (i <  size(d)):
	if(d[i] < recorde):
		s = s + 1
	i = i + 1

print (recorde)
print (s)

	