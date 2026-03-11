from numpy import*

C = array(eval(input("Digite as temperatura: ")))
i = 0
j = 0
cont = 0
while(i < size(C)):
	if(C[i] >= -100):
		cont = cont + 1
	i = i + 1

Cr = array(zeros(cont, dtype = float))
i = 0
while(i<size(C)):
	if(C[i] >= -100):
		Cr[j] = C[i]
		j = j + 1
	i = i + 1
print(Cr)