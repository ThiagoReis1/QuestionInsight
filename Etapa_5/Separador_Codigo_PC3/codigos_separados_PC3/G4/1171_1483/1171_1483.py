n = int(input("digite o numero total: "))
i = 1
j = 3
s = 0
k = 1
while i <= n:
	s = s + ((i**3) / (2 + j)) * k
	i = i + 1
	j = j + 2
	k = k * (-1)
print(round(s , 8))