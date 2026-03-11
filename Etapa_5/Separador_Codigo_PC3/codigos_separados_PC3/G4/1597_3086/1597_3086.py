from numpy import*
v = array(eval(input("v: ")))
a = 0
for i in v:
	if(i > 80):
		i = i - 5
		a = a + 1
print(round(sum(v), 2))	