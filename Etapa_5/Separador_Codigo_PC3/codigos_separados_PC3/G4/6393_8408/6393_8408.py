from numpy import*

num = array(eval(input("senha: ")))

for i in range(num):
	if num[9] == 9:
		num[9] = num[0]

for i in range (size(num)):
	num[i] = num[i]+1
	num[i] = num[i]**3
	

print(num)

