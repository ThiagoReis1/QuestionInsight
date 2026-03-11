from numpy import*

vet = array(eval(input("Digite o custo de cada item: ")))

desc = 0

for i in range(size(vet)):
	if (vet[i]>160):
		desc = desc + 25.0
		
total = sum(vet) - desc
print(round(total,2))
	