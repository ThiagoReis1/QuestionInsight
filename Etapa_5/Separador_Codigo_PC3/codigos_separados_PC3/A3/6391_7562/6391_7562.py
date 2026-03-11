from numpy import* 

num = array(eval(input("Insira o codigo: ")))

prede = zeros(size(num), dtype= int)

for i in range(size(num)):
	if num[i] == 0:
		num[i] = 9**3
	else:
		num[i] = (num[i]- 1)**3
		
print(num)