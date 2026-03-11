from numpy import*

n = array(eval(input("digite a face tirada: ")))
i = 0

while i < size(n):
	if n == 1:
		i = i/2
	elif n == 2:
		i = i*3
	elif n == 3:
		i = i/2
	elif n == 4:
		i = i*3
	elif n == 5:
		i = i/2
	elif n == 6:
		i = i*3
print(round(i, 2))