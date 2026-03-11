from numpy import *
from numpy.linalg import *

pagar = array(eval(input("valor: ")))
pagar = pagar.T

sistemas = array([[1,1], [0.25,0.5]])

moedas = dot(inv(sistemas), pagar)

print(moedas)