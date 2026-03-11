from numpy import *

s = input("string = ")
s = s.split(",")

z = zeros(5 , dtype = int)

for i in s:
	if i == "BE":
		z[0] = z[0] + 1
	elif i == "ES":
		z[1] = z[1] + 1
	elif i == "FR":
		z[2] = z[2] + 1
	elif i == "IT":
		z[3] = z[3] + 1
	elif i == "PT":
		z[4] = z[4] + 1

print(max(z))
print(z)