from numpy import*
vet = array(eval(input("custo: ")))

i = 0
while(i<size(vet)):
	if(vet[i]>=80):
		vet[i] = vet[i]*0.85
	i = i + 1
print(round(sum(vet),2))