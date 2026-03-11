from numpy import*
from numpy.linalg import*

b = array(eval(input()))



a = array([[1, 1], [0.25,0.5]])


p = dot(inv(a),b.T)
print(p)
