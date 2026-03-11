string = input("produto: ").upper()

i = 0

m = 7.25
p = 4.75
r = 3.50

maxi = len(string)
acum = 0

while i < maxi:
	if string[i] == 'M':
		acum += m
	elif string[i] == 'P':
		acum += p
	elif string[i] == 'R':
		acum += r
	i+= 1
print(round(acum, 2))