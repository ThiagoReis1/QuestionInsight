from numpy import *

senha = array(eval(input("Digite os numeros da senha: ")))

for i in range (size(senha)):
	senha[i] *= 2

print(senha)