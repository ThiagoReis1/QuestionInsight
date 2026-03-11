from numpy import *

v = array(eval(input("Saques: ")))

saque_abaixo = 0

for i in range(size(v)):
	if v[i] <= 50:
		saque_abaixo = saque_abaixo + 1

s = zeros(saque_abaixo, dtype = int)
o = 0

for j in range(size(s)):
	if v[i] <= 50:
		s[j] = o
	o = o + i

print(saque_abaixo)
print(s)
		