from numpy import*

n = array(eval(input("Digite aqui: ")))

total = 0
i = 0

while i < size(n):
	if n[i] == 1:
		total = total + 100
	elif n[i] == 2:
		total = total + 60
	elif n[i] == 3:
		total = total + 20
	elif n[i] == 4:
		total = total + 0
	i = i + 1
print(total)