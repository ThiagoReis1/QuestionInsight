from numpy import*

custo = array(eval(input("Digite os custos:")))
i = 0

while(i < len(custo)):
	if(custo[i] > 80):
		custo[i] = custo[i] - (custo[i] * 0.15)
		i = i + 1
		
	else:
		i = i + 1

total = sum(custo)
print(round(total,2))