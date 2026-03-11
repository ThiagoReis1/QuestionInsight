from numpy import *

plv = input("palavra:").upper()

i = 0 
total = 0

while i < len(plv):
	if plv[i] == "A" or plv[i] == "E" or plv[i] == "I" or plv[i] == "O" or plv[i] == "U":
		total = total + 45.15
	else:
		total = total + 50.17
	i = i + 1

print(round(total, 2))
		
