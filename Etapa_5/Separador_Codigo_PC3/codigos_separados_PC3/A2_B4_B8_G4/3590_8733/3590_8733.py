from numpy import*

dado = array(eval(input("face do dado: ")))
p = 0
i = 0

while i < size(dado):
	if dado[i] == 1:
		p = p + 10
	elif dado[i] == 2:
		p = p + 5
	elif dado[i] == 3:
		p = p
	elif dado[i] == 4:
		p = p + 5
	elif dado[i] == 5:
		p = p + 20
	elif dado[i] == 6:
		p = p + 10
	i = i + 1
	
print(p)