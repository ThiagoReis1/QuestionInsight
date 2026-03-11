#Cogido secreto
from numpy import *
num = array(eval(input("Numero: ")))

for i in range(size(num)):
	if num[i] == 0:
		num[i] = 9
	else:
		num[i] = num[i] - 1
print(num)