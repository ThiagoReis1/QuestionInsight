from numpy import *
from numpy.linalg import *

a = array(eval(input("digite: ")))

x = min(a)
y = sum(a)
b = y-x
c = b/(size(a)-1)
	
print(round(c, 2))	
