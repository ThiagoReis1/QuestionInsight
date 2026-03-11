from numpy import *

t = array(eval(input()))
ip = 0

for i in range(size(t)):
	if t[i] % 5 == 0:
		ip +=1
		
ind = zeros(ip, dtype=int)
print(ip)
j = 0
for i in range(size(t)):
	if t[i] % 5 == 0:
		ind[j] = i
		j += 1
print(ind)