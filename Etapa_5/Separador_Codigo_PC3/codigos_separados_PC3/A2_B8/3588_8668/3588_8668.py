from numpy import*

aneis = array(eval(input()))
i = 0
total = 10000
while i < size(aneis):
	if aneis[i] == 1:
		total = total * 2
	elif aneis[i] == 2:
		total = total 
	elif aneis[i] == 3:
		total = total / 2
	elif aneis[i] == 4:
		total = total / 4
	i += 1
print(round(total, 2))
	