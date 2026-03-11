from numpy import*
from numpy.linalg import*
pagar = array(eval(input("")))
pagar = pagar.T

sistema = array([[1,1],
					 [0.25,0.5]])
# 1*x + 1*y = moedas|inverso: 2 -4
									
moedas = dot(inv(sistema),pagar)
print(moedas)