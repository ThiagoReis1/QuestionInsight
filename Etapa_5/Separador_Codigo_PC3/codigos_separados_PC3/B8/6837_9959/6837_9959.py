iogurtes = 3.75
massas = 4.50
salgadinhos = 2.90

x = input().upper()

i = 0
total = 0

while i < len(x):
	if x[i] == 'I':
		total = total  + iogurtes
	elif x[i] == 'M':
		total = total + massas
	elif x[i] == 'S':
		total = total + salgadinhos
	i = i + 1

print(round(total,2))