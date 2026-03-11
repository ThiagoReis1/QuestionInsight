from numpy import *

# Entries

states = input("Insert states: ")

# Definitions

states = states.split(',')
s = size(states)
base = zeros(5, dtype=int)

# Processing

for s in range(s):
	if(states[s] == "AM"):
		base[0] += 1
	elif(states[s] == "PE"):
		base[1] += 1
	elif(states[s] == "MG"):
		base[2] += 1
	elif(states[s] == "SP"):
		base[3] += 1
	elif(states[s] == "RS"):
		base[4] += 1
		
print(max(base))		
print(base)
