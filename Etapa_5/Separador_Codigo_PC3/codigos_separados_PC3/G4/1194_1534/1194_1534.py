#Suenne Renata Lima Fernandes- 21602342
from numpy import *

v = array (eval (input ("Vetor:")))

i = 0
t = 0

while (i < size (v)):
	if (v[i] > -100):
		t = t + 1
	i = i + 1
vn = array (zeros (t, dtype = float))
i = 0
j = 0

while (i < size (v)):
	if (v[i] > -100):
		vn[j] = v[i]
		j = j + 1
	i = i + 1
print (vn)
	