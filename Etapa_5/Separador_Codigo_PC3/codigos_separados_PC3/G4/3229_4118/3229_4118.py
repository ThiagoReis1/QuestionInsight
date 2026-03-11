from numpy import*
from numpy.linalg import*
A = array([[1,1],[0.25,0.5]])
B = array(eval(input("tal coisa ai: ")))
B = B.T
X = dot(inv(A), B)
print(X)