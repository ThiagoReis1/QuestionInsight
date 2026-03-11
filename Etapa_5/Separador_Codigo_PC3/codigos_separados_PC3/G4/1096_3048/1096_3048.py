num = int(input("numero fornecido: "))

ab = (num // 10000) 
cd = (num % 10000) // 100
ef = (num % 1000) // 1

soma = (ab**3) + (cd**3) + (ef**3)

if(soma == num): 
	print("atende")
	print(num)
else:
	print("nao atende")
	print(num)
