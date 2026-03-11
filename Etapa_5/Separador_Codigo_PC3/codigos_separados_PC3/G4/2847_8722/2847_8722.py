from numpy import*
num = array(eval(input("Digite os numeros: ")))
cod = zeros(size(num), dtype=int)

for i in range(size(num)):
	if num[i] >= 0 and num[i] <= 9:
		cod[i] = num[i]**2
	
print(cod)