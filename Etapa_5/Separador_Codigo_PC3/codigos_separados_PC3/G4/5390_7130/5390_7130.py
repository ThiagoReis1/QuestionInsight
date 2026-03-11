from numpy import*

r = input()
v = 0.19
c = 0.23
i = 0
acum = 0

while i < len(r):
	if r[i].upper() == "A" or r[i].upper() == "E" or r[i].upper() == "I" or r[i].upper() == "O" or r[i].upper() == "U":
		acum = v + acum
	else:
		acum = c + acum 
	i = i + 1
print(round(acum,2))
