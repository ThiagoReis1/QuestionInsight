from numpy import*

i = 0
p = 0

ci = array(eval(input('incira o custo dos itens: ')))

while i < size(ci):
	if ci[i] > 40:
		p = p + ci[i] - 2.5
	else:
		p = p + ci[i]
	i += 1
print(round(p,2))