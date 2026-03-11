from numpy import *

s = input().upper().split(",")
mp = {"C":0, "O":1, "P": 2, "E": 3}
z = zeros(4, dtype=int)

for i in s:
	if i in mp:
		z[mp[i]] = z[mp[i]] + 1
print(z)
		