from numpy import*
v = array(eval(input("vetor: ")))
c = 0
for i in v:
	if i == 88:
		c = c / 2
	else:
		c += i
print(c)