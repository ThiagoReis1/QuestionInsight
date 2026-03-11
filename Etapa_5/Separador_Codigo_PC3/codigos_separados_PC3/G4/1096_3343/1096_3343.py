num = int(input("num:"))

n_1 = num // 10000
r_1 = num%10000

n_2 = r_1 // 100
r_2 = r_1 % 100

if	num == ((n_1**3)+(n_2**3)+(r_2**3)):
	print("atende", num)

else:
	print("nao atende", num)
	