num = float(input(""))
soma=0
while(num!=0):
	soma = soma + num
	num = float(input(""))
	if(num==0):
		print(soma)
		print(round(soma,2))