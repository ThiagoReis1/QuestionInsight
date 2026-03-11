from numpy import*
x = array (eval(input ("Digite vetor: ")))
t = 0
for i in range (size(x)):
	if (x[i] % 5 == 0) :
		t = t + 1
vet = arange(t)
print (t)
k = 0 
for i in range (size(x)):
	if (x[i] % 5 == 0):
		vet[k] = i
		k = k + 1
print (vet)