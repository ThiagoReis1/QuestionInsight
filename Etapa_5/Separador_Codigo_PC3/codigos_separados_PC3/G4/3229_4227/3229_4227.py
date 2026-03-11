from numpy import*
from numpy.linalg import*
p = array(eval(input()))
p = p.T

s = array([[1,1],
				[0.25,0.5]])
print(solve(s,p))