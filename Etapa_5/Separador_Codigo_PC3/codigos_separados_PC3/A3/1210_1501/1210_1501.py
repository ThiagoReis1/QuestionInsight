from numpy import*
vet = array(eval(input("distancia: ")))
i = 0
k = 0
recorde = 74.08
while(i < size(vet)):
	if(vet[i] < recorde):
		k = k + 1
	i = i + 1
vet_1 = array(zeros(size(vet), dtype = float))
print(recorde)
print(k)