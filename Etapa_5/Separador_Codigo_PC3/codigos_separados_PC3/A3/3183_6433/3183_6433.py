from numpy import *

v = array(eval(input("vetor: ")))

new = zeros(size(v), dtype = int)
count = 0

for i in range(size(v)):
	count = size(v)-1 - i
	new[count] += v[i]
	

print(new)