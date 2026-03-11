from numpy import *

record = 307

x = array(eval(input("Digite os pesos: ")))

i = 0
j = 0
while(i < size(x)):
	if(x[i] > record):
		j = j + 1
	i = i + 1
print(record)
print(j)