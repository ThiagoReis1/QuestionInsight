from numpy import *

v1 = input('Digite as cores: ').upper().split(',')


v2 = zeros(5, dtype=int)
for i in range(size(v1)):
	if v1[i] == 'P':
		v2[0] = v2[0] + 1
		
	if v1[i] == 'C':
		v2[1] = v2[1] + 1
		
	if v1[i] == 'R':
		v2[2] = v2[2] + 1
		
	if v1[i] == 'L':
		v2[3] = v2[3] + 1
		
	if v1[i] == 'B':
		v2[4] = v2[4] + 1

print(max(v2))
print(v2)

