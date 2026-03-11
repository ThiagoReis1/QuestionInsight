from numpy import *
a = array(eval(input("Digite a pontuacao total")))
p = 100
i = 0
while i < size(a):
	if a[i] == 1:
		p = p * 5
	elif a[i] ==2:
		p = p * 3
	elif a[i] == 4:
		p = p / 2
	i = i + 1

print(round(p, 2))
		