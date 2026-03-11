from numpy import*

pl = input("").upper()
vogal = 45.12
conso = 50.18
i = 0
acum = 0

while i < len(pl):
	if pl[i] == "A" or pl[i] == "E" or pl[i] == "I" or pl[i] == "O" or pl[i] == "U":
		acum = acum + vogal
	else:
		acum = acum + conso
	i = i +1
print(round(acum,2))