from numpy import*

vet= array(eval(input("Digite o vetor: ")))

recorde = 74.08
i=0
count=0

while(i < size(vet)):
	if(vet[i] <= recorde):
		count = vet[i] + 1
	i= i + 1
else:
	print(recorde)

i=0
count=0
while( i > size(vet)):
	if(vet[i] >= recorde):
		count = vet[i] + 1
	i = i + 1
print(count)
