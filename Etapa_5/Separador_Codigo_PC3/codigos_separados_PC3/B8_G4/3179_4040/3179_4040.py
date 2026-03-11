from numpy import *

# Entries

vec = array(eval(input("Insert desired vector: ")))

# Definitions

s = size(vec)
r = size(vec)
t = 0
defi = zeros(s, dtype=int)

# Processing


for i in range(s):
	if(vec[i] == 1):
		defi[r-1] += 1
		r += -1
	elif(vec[i] != 1):
		defi[t] += vec[i]
		t += 1
		
print(defi)