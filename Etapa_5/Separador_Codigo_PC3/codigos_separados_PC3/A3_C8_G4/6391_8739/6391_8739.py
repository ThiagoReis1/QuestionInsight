from numpy import*

vetor = array(eval(input("numeros: ")))
a = []

for num in vetor:
	num = int(num)
	x = (num - 1) ** 3
	if num == 0:
		x = 9 ** 3
#	if num >= 9:
#		x = 0
	a.append(x)
print(array(a))