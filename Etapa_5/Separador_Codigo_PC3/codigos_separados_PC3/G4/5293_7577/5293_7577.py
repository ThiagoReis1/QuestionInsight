num = 0 

var = int(input("entrada: "))
while(var != num):
	num = var /100
	soma += num
	soma = 1
	var = int(input("entrada: "))
	print(round(soma,2))