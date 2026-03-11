from numpy import *
from math import *

v = array(eval(input("Digita ai: ")))

i = 0
MG = 1

while (i < size(v)):
	MG = (MG * v[i])
	i = i + 1

media = MG ** (1 / size(v))	
print(round(media, 2))