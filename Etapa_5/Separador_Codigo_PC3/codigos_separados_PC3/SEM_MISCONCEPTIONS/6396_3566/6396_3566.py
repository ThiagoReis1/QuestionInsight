from numpy import *

entrada = eval(input())
final = []
for i in range(len(entrada)):
	final.append(entrada[i]*2)

print(array(final))