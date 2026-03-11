from numpy import *
str = input().upper()
vogais = ['A', 'E', 'I', 'O', 'U']
sum = 0
for char in str:
	if char in vogais:
		sum += 35.15
	else:
		sum += 42.17
print(round(sum, 2))