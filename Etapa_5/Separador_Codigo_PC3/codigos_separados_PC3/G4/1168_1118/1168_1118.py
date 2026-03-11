n = int(input())
i = 1
s = 0
while i < (n+1):
	s += (-1)**(i) * i**3 /(8 + (2*(i-1) + 1))
	i += 1
print(round(s, 5))