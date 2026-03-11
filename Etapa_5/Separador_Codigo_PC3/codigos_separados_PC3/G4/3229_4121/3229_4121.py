from numpy import*
from numpy.linalg import*
qm = array(eval(input()))
qm = qm.T

pag = ([[1,1],[0.25,0.5]])
mod =dot(inv(pag),qm)

print(mod)