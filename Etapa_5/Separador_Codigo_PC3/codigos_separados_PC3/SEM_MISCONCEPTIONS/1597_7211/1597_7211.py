from numpy import*

custo = array(eval(input("custo do produto: ")))

i=0
total = 0
while(i < size(custo)):
	if(custo[i]>80):
		total = total + custo[i] - 5
	else:
		total = total + custo[i]
	i=i+1
print(round(total,2))
