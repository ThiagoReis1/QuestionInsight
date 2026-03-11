x = int(input(""))
k = int(input(""))
soma = 0
i = 0
j = -1
while(i < k):
	
	soma =(x**(2 * i + 3))/(2 * i + 3)*j
	j = j * (-1)
	i = i + 1
print(round(soma,6))