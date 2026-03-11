
from numpy import*
aneis = array(eval(input("")))
pont = 0
i = 0
while i < size(aneis):
	if aneis[i] == 1:
	   pont = pont +80
	elif aneis[i] == 2:
	   pont = pont +40
	elif aneis[i] == 3:
	   pont = pont +20
	elif aneis[i] == 4:
	   pont = pont +10
	i += 1
print(round(pont,2))