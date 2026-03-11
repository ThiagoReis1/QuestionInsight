from numpy import*
n = array(eval(input("pontos: ")))
i = 0
c = 10000
tan = size(n)
while i < tan:
	if n[i] == 1:
		c = c * 2
	elif n[i] == 2:
		c = c 
	if n[i] == 3:
		c = c / 2
	elif n[i] == 4:
		c = c / 4
	i = i +1
print(round(c,2))