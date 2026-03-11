from numpy import*

v = input("").upper()

i = 0
som = 0

while(i<len(v)):
	if v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U":
		som = som + 45.12
	else:
		som = som + 50.18
	i = i + 1

print(round(som,2))
		
