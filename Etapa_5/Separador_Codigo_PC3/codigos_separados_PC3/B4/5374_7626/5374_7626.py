from numpy import*

string= input("").upper()
i= 0
v= 0
while i < len(string):
	if string[i] == "A":
		v= v+ 0.15
	elif string [i] == "E":
		v= v + 0.15
	elif string[i] == "I":
		v =v + 0.15
	elif string[i] == "O":
		v= v + 0.15
	elif string[i] == "U":
		v= v + 0.15
	else:
		v= v + 0.17
	i = i + 1
print(round(v, 2))