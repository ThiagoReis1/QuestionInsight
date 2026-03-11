from numpy import *

cor = array(eval(input("Tempo do corredor: ")))

i = 0

while (cor[i] != min(cor)):
	i = i + 1
	
print (i)