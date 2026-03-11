from numpy import*
j = array(eval(input("Digite as jogadas: ")))
i = 0
s = 0
while i < size(j):
	if j[i] == 1:
		s = s + 10
	elif j[i] == 2:
		s = s + 5
	elif j[i] == 4:
		s = s + 5
	elif j[i] == 5:
		s = s + 20
	elif j[i] == 6:
		s = s + 10
	i = i + 1
print(s)