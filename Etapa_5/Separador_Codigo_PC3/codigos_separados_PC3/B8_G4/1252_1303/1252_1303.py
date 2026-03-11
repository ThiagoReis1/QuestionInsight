#Johnathan Dias			#Matricula: 21651445
from numpy import*

vet = array(eval(input("Digitar o Vetor: ")))

a = min(vet)
b = max(vet)
c = (0.6 * a) + (0.4 * b)
d = (0.3 * a) + (0.7 * b)
w = array(zeros(2, dtype = int))
for i in vet:
	if (i>= a and i<c):
		w[0] = w[0] + 1
	elif (i >= c and i < d):
		w[1] = w[1] + 1
print(w)
	