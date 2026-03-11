n = int(input("Informe um numero: "))

f_step = n // 10

s_step = f_step // 10

t_step = n % 100


if(((s_step**2) + (t_step**2)) == n):
	print("atende")
	print(n)
else:
	print("nao atende")
	print(n)