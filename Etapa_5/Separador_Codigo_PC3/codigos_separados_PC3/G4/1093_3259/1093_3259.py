num = int(input("Digite o numero: "))

n_1 = num // 100
n_2 = num % 100
n_3 = (n_1 ** 2) + (n_2 ** 2)

if ( num == n_3):
	 print("atende", num)
	 
else:
	 print("nao atende", num)