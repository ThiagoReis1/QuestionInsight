from numpy import*

senha = array(eval(input(":")))
num = zeros(size(senha),dtype=int)

for i in range (size(senha)):
	if senha[i] == 0:
		num[i] = 9 ** 2
	else:
		num[i] = (senha[i] - 1) ** 2
print(num)