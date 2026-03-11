from numpy import *
aneis = array(eval(input("")))
pont = 10000
i = 0
while i < size(aneis):
	if aneis[i] == 1:
		pont *= 2
	if aneis[i] == 3:
		pont /= 2
	if aneis[i] == 4:
		pont /= 4
	i += 1
print(round(pont,2))