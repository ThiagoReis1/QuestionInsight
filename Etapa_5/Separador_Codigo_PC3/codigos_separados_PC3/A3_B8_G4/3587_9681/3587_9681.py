from numpy import *
num = array(eval(input("Quais alvos acertou? ")))
mu = array([5,3,1,2])
p = 100
i = 0
a = size(num) - 1
while i <= a:
	if num[i] == 1:
		p = (p*5)
	elif num[i] == 2:
		p = (p*3)
	elif num[i] == 3:
		p = (p*1)
	elif num[i] == 4:
		p = (p/2)
	i += 1
print(round(p,2))	