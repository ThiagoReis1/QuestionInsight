from numpy import *

# Entries

vec = array(eval(input("Insert number of students per class: ")))

# Definitions

np = 0
en = 0
s = size(vec)

# Processing

for i in range(s):
	if(vec[i]%2 == 0):
		np += 1
print(np)

p = zeros(np, dtype=int)  # New Definition

for i in range(s):
	if(vec[i]%2 == 0):
		p[en] += i
		en += 1

print(p)