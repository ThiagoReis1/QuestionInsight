from numpy import*

nota = array(eval(input()))
a = 8
b = 2

i = 0


while i < size(nota):
	if nota[i] > a:
		nota[i] = 10
	if nota[i] < b:
		nota[i] = 0
	i = i + 1
print(nota)
		
		