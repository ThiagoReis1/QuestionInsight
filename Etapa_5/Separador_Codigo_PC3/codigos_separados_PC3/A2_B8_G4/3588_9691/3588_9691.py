from numpy import*
num = array(eval(input("insira as notas : ")))
i = 0
t = size(num) - 1
j1 = 10000

while i <= t:
	if num[i] == 1:
		j1 = j1*2
	elif num[i] == 2:
		j1 = j1
	elif num[i] == 3:
		j1 = j1/2
	elif num[i] == 4:
		j1 = j1/4
	i += 1
print(round(j1 , 2))