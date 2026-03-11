from numpy import*
from numpy.linalg import*
x = array(eval(input()))
z = x.min()
y = (sum(x)-z)/(size(x)-1)
print(round(y,2))