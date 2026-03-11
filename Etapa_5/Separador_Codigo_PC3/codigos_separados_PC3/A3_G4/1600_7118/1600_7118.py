from numpy import*

custo = array(eval(input()))

c = 80
i = 0
cont = 0

while i < size(custo):
	if custo[i] > c:
		custo[i] = custo[i] - (custo[i] * 15/100)
	
	i = i + 1

print(round(sum(custo), 2))
