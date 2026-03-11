from numpy import *

chuveiro = array(eval(input()))
tempo = array(eval(input()))

sum = 0

for i in range(len(chuveiro)):
	agua = ((chuveiro[i]*5)/100) * tempo[i]
	sum += agua
	
print(round(sum,2))