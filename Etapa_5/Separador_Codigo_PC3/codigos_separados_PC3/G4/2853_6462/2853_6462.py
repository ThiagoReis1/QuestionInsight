from numpy import *
s = array(eval(input()))
soma = 0
for i in range(size(s)):
	if s[i] != 10:
		soma = soma + s[i]
	else:
		soma = soma * 10
print(soma)
