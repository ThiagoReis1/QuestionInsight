from numpy import *
from numpy.linalg import *

vet = array(eval(input("Digite as notas: ")))

for i in range(shape(vet)[0]):
	if (vet[i] >= 0):
		print(max(vet))

