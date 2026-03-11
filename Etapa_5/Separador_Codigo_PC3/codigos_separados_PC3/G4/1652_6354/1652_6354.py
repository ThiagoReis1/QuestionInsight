from numpy import *

s = (input("Digite a cor: ")).upper().split(',')
z = zeros(5, dtype = int)
for i in range (size(s)):
	if s[i] == "B":
	   z[0] = z[0] + 1
	elif s[i] == "PA":
		z[1] = z[1] + 1
	elif s[i] == "PR":
		z[2] = z[2] + 1
	elif s[i] == "A":
		z[3] = z[3] + 1
	else:
		z[4] = z[4] + 1
print(max(z))
print(z)






