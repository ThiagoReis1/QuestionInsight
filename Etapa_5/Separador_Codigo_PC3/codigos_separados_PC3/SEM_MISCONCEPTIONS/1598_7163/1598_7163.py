from numpy import*

preco = array(eval(input("custo: ")))
i = 0
s = 0
while i < size(preco):
	if preco[i] > 90:
		s = s + (preco[i] - 6.50)
		i =  i + 1
	else:
		s = s + preco[i]
		i = i + 1
print(round(s,2))
	