from numpy import*

s = input().upper()
i = 0
v = 0
c = 0

for letra in s:
	if letra in "A, E, I, O, U":
		v = v + 1
		tv = v*45.15
	else:
		c = c + 1
		tc = c*50.17
		
total = tv + tc
print(round(total,2))