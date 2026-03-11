from numpy import*

nota = array(eval(input()))
i = 0

while i < size(nota):
	if nota[i] > 4 and nota[i] <= 5:
		nota[i] = 4
	if nota[i] > 9 and nota[i] <= 10:
		nota[i] = 10
	i = i + 1
print(nota)