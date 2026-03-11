from numpy import *

senha = array(eval(input()))

for i in range(size(senha)):
	senha[i] = senha [i] * 2
print(senha)