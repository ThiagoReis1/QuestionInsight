from numpy import*
v = input("palavra: ").upper()

i = 0 
j = 0
while i < len(v):
	if v[i] == "A":
		j = j +  45.15
	elif v[i] == "E":
		j =  j + 45.15
	elif v[i] == "I":
		j = j + 45.15 
	elif v[i] == "O": 
		j = j + 45.15 
	elif v[i] == "U":
		j = j + 45.15
	else:
		j = j + 50.17

	i = i +1 
print(round(j,2))