from numpy import *
from numpy.linalg import *
pagar= array(eval(input()))
pagar= pagar.T

sistema= array([[1,1],
				  [0.25, 0.5]])
# 1*x + 1*Y = moeadas        inverso: 2 -4
# 0.25*x + 0.25*y = valor    inverso: -1 4

moedas= dot(inv(sistema),pagar)
print(moedas)