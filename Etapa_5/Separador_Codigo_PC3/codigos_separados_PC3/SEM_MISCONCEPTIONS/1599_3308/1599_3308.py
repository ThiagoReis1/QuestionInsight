from numpy import*
vety = array(eval(input("digite o vetor preço itens:")))
i = 0
pfinal= 0

while(i<size(vety)):
	if(vety[i]>80):
		pfinal = pfinal + vety[i] - vety[i]*(0.15)
	else:
		pfinal = pfinal + vety[i]
	i = i + 1
print(round(pfinal,2))