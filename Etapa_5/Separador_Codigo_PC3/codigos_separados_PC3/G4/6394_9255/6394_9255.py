from numpy import *

spy = array(eval(input("Insira o codigo: ")))
i = 0
cont = zeros(size(spy), dtype = int)

for i in range(size(spy)):
	if spy[i] < 9:
		cont[i] = spy[i] + 1
	else:
		cont[i] = 0
print(cont)