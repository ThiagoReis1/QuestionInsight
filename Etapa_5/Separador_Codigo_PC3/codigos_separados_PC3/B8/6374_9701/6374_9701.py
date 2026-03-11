from numpy import *
s = input().upper().split(',')
quant = zeros(4,dtype=int)

for i in range(size(s)):
	if s[i] == "O":
		quant[0] += 1
	elif s[i] == "D":
		quant[1] += 1
	elif s[i] == "N":
		quant[2] += 1
	elif s[i] == "C":
		quant[3] += 1
print(quant)