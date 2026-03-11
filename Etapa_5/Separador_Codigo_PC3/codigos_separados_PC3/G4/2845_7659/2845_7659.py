from numpy import*

num = array(eval(input("digite a senha: ")))

soma = zeros(size(num), dtype=int)

for i in range(size(num)):
	if num[i] >= 0 and num[i] <= 9:
		soma[i] = num[i] + 1
	if num[i] == 9 :
		num[i] = 0
		soma[i] = num[i]

print(soma)