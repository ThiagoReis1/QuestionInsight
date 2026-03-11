from numpy import *
cod = array(eval(input("insira o codigo: ")))
cod_n = zeros(size(cod), dtype = int)
				  
for i in range(size(cod)):
	cod_n[i] = cod[i] *2
print(cod_n)