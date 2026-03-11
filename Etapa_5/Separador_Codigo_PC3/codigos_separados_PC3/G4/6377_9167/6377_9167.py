from numpy import *

s = input("aa:  ").split(',')

novo = zeros(4, dtype=int)

for i in range(size(s)):
	if s[i] == 'A':
		novo[0] = novo[0] + 1
	if s[i] == 'B':
		novo[1] = novo[1] + 1
	if s[i] == 'C':
		novo[2] = novo[2] + 1
	if s[i] == 'D':
		novo[3] = novo[3] + 1
print(novo)