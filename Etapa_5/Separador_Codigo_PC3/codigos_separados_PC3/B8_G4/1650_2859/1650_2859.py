from numpy import *
v = input("Cores: ").upper().split(',')

cont = zeros(5, dtype=int)

c_p = 0
c_c = 0
c_r = 0
c_l = 0
c_b = 0

for i in v:
	if(i == 'P'):
		c_p = c_p + 1
	elif(i == 'C'):
		c_c = c_c + 1
	elif(i == 'R'):
		c_r = c_r + 1
	elif(i == 'L'):
		c_l = c_l + 1
	elif(i == 'B'):
		c_b = c_b + 1

cont[0] = c_p
cont[1] = c_c
cont[2] = c_r
cont[3] = c_l
cont[4] = c_b

print(max(cont))
print(cont)