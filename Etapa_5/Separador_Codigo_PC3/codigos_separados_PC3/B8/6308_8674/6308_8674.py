from numpy import*

valores = input().upper()

total = 0.0
i = 0 
a = 0
l = 0
p = 0

while i < len(valores):
	if valores[i] == "A":
		total = total + 16.75
		a += 1 
	elif valores[i] == "L":
		total = total + 4.60
		l += 1
	elif valores[i] == "P":
		total = total + 2.85
		p += 1
	i += 1 
print(round(total, 2), a , l, p)