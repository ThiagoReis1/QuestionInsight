from numpy import *
from numpy.linalg import *
pagar = array(eval(input("Quantidade de Moedas: ")))
pagar = pagar.T

sist = array([[1,1],
				 [0.25,0.5]])
#1^x + 1^ŷ = moedas | inverso 2 -4
#0.25^x + 0.5^y = valor | 		-1 4
moedas = dot(inv(sist), pagar)

print(moedas)