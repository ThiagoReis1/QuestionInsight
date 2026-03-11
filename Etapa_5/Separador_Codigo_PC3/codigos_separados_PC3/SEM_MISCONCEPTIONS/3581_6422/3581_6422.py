from numpy import*

custo = array(eval(input("custo total da compra: ")))
i = 0
c = 0

while i < size(custo):
	if custo[i]>40:
		c = c + 1#c - 2.50
	
	i = i + 1
total = sum(custo) - c*2.50
print(round(total, 2))