from numpy import*

v = input().upper()
i = 0
b = 0
c = 0

while i < len(v):
	if v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U":
		c = c + 25.12
	else:
		b = b + 40.18
	i = i + 1
total = c + b
print(round(total,2))		