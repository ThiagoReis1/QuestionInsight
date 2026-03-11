from numpy import *

codigo = array(eval(input("Digite: ")))

for i in range(size(codigo)):
	codigo[i] = codigo[i] ** 2
	
print(codigo)