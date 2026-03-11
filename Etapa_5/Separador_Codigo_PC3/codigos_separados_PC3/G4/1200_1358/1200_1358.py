from numpy import*
vetor = array(eval(input("Informe o valor do vetor: ")))
i = 0
cont = 0
x = (zeros(size(vetor),dtype = float))
while(i < size(vetor)):
	if(vetor[i] >= 0):
		x[i] = vetor[i]
		cont = cont + 1
	i = i + 1

x2 = (zeros(cont,dtype = float))
s = 0
y = 0
while(s < size(x)):
	if(x[s] > 0):
		x2[y] = x[s]
		y = y + 1
	s = s + 1
print(x2)