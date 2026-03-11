from numpy import *
from numpy.linalg import *

pagar = array(eval(input("Digite a quantidade de moedas/valor: ")))

pagar = pagar.T

sistema = array([[1,1],[0.25, 0.50]])

moedas = dot(inv(sistema), pagar)

print(moedas)