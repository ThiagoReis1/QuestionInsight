from numpy import*
v = array(eval(input("Insira as distancias:")))
i = 0
j = 0
recorde = 74.08

while (i < size(v)):
	if(v[i] > 74.08):
		j = j + 1
	i = i + 1
	
print(recorde)
print(j)