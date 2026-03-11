x = float(input())
k = int(input())

c = 0
i = 0


while k > i:
	c = c + (x**(2*i+1))/(2*i+1)
	i = i+1

print(round(c, 7))