from numpy import*

custo = array(eval(input("")))
n = size(custo)
i = 0
while(i < n):
	if(custo[i] > 80):
		custo[i] = custo[i] - (15/100)*custo[i]
	
	else:
		custo[i]=custo[i]
	i = i + 1
print(round(sum(custo),2))
		