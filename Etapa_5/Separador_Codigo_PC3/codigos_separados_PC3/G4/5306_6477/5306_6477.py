x = float(input('type a value for x: '))
k = int(input('type for the terms: '))
den = 2
a = 0 
eq = 0

while(a<k):
	eq = eq+(x/den)
	a = a+1
	den = den+2

print(round(eq, 8))
	