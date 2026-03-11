import numpy as np

valores = np.array(eval(input()),np.float)
smt = 0
for i in valores:
	smt = smt+(i**(1/3))
	
saida = (smt/np.size(valores))**3

print(round(saida,2))