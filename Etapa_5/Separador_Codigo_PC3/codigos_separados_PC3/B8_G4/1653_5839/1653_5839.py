from numpy import *
s = input("Digite as nacionalidades: ").upper().split(',')
x = size(s)

new = zeros(5 , dtype=int)

for i in range(0,x):
	if (s[i] == "AR"):
		new[0] = new[0] + 1
	elif (s[i] == "BR"):
		new[1] = new[1] + 1
	elif (s[i] == "CL"):
		new[2] = new[2] + 1
	elif (s[i] == "CO"):
		new[3] = new[3] + 1
	elif (s[i] == "UY"):
		new[4] = new[4] + 1
		
print(max(new))	
print(new)