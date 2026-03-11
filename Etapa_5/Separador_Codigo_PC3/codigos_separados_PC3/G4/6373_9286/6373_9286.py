from numpy import *
v = input("Livros:").upper().split(',')
s = zeros(4 , dtype=int)

for i in range(len(v)):
	if v[i] == 'A':
		s[0] +=1
	if v[i] == 'P':
		s[1] += 1
	if v[i] == 'D':
		s[2] += 1
	if v[i] == 'M':
		s[3] += 1
	
print(s)
