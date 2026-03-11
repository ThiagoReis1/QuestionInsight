from numpy import *
from numpy.linalg import *


tempo = array(eval(input("")))

i = 0 
 
while( i != size(tempo)):
	if(tempo[i] == max(tempo)):
		print(i)
	i = i + 1