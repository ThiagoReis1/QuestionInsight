num = int(input("informe um numero: "))

met1 = (num // 1000) 
met2 = (num%1000)

soma = (met1 + met2)**2

if (soma == num):
	print("atende")
	print(num)
	
else:
	print("nao atende")
	print(num)