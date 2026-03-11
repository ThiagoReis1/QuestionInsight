from numpy import*

saltos = array(eval(input()))

s = 0
i = 0
recorde = 2.5

while(i<size(saltos)):
	if(saltos[i] < recorde):
		s = s + 1
	i = i + 1

print(recorde)
print(s)



