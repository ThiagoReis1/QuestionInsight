from numpy import *

v1 = array(eval(input("Vetor:")))

i = 0
a = 0
b = 0

while (i < size(v1)-1):
	if (v1[i] <= v1[i+1]):
		a = a + 1
	else:
		b = b + 1
	i = i + 1	
	
if (b == 0):
	print("True")
else:
	print("False")
