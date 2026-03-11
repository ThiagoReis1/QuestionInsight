n = int(input())
s = 0
i = 1
while (i < (n+1)):
	s += (-1)**(i - 1) * (i**2)/(1 + ((2 * i) + 1))
	i += 1
print(round(s,7))