from numpy import*
y = array(eval(input("v: ")))
a = 0
for i in y:
	if(i > 80):
		i = i - 5
		a = a + 1
print(round(sum(y), 2))