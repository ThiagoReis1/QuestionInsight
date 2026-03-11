import numpy as np
notas_str = input("Digite as notaas no formato [x0, x1, xn]: ")
notas = eval(notas_str)
pesos = [2,2,6,1]

if len(notas) == len(pesos):
	media_ponderada = round(np.dot(notas,pesos)/np.sum(pesos), 2)
	print(media_ponderada)
else:
	print("o numero de notas tem que ser igual o numero de pesos")