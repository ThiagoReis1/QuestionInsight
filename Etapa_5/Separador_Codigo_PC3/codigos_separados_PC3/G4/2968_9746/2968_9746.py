l = input()
q = int(input())
t = int(input())

if l == "L":
	x = 5
else:
	x = 3.5

r = t * 4	
y = (q * x) + r

print(round(y, 2))