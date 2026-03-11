from numpy import*
p = input("qual o produto:  ").upper()
i = 0 
ac = 0
a = 0
l = 0
p2 = 0
while i < len(p):
	if p[i] == "A":
		ac += 19.90
		a += 1 
	elif p[i] == "L":
		ac += 3.50
		l += 1
	elif p[i] == "P":
		ac += 4.25
		p2 += 1
	i = i +1 
print(round(ac,2), a, l, p2)

		