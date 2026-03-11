n = int(input("digite o numero: "))
i = 1
j = 1
s = 0
k = 1
while i <= n:
	s = s + ((i**2) / (4 + j)) * k
	i = i + 1
	j = j + 2
	k = k * (-1)
print(round(s , 8))