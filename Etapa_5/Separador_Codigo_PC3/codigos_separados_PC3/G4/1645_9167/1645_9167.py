from numpy import *

s = array(eval(input("aa:  ")))
cont = 0

for i in range(size(s)):
	if s[i]>=2000:
		cont += 1
print(cont)
novo = zeros(cont, dtype=int)

j = 0
for i in range(size(s)):
	if s[i] >= 2000:
		novo[j] = i
		j += 1
print(novo)