from numpy import*
from numpy.linalg import*

q1 = array(eval(input("q1: ")))
q1 = q1.T
m = array([[1,1], [0.25,0.5]])

q2 = dot(inv(m),q1)

print(q2)