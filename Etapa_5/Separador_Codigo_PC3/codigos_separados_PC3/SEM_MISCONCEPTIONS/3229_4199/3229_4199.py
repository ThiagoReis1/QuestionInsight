from numpy import *
from numpy.linalg import *
pagar = array(eval(input("quantidade de moedas: "))) #vetor
pagar = pagar.T #necessario transpor

sistema = array([[1,1],[0.25,0.5]]) # sistema linar

moedas = dot(inv(sistema), pagar) # encontrar x e y 
print(moedas)
