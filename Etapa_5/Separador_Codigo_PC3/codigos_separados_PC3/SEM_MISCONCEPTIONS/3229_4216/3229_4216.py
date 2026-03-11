from numpy import*
from numpy.linalg import*
vetor = array(eval(input("qnt: ")))
vetor = vetor.T

sistema = array([[1,1],
					  [0.25,0.5]])
m = dot(inv(sistema),vetor)
print(m)