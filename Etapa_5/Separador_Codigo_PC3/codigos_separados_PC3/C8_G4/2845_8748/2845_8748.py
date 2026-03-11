from numpy import*

vetor = array(eval(input("manda: ")))
a = []

for num in vetor:
	num = int(num)
	x = num + 1
	if x > 9:
		x = 0
	a.append(x)
print(array(a))



