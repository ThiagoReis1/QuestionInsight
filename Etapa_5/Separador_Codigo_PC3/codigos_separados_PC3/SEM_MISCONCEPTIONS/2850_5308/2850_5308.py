from numpy import*

entrada = array(eval(input(" ")))

total = 0


for i in range(size(entrada)):
	total = total + entrada[i]
	if total >= 55:
		total = 0
	
print(total)