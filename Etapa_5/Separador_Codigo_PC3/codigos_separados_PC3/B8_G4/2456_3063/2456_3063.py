v = float(input("digite o valor da mensalidade: "))
n = int(input("digite o numero de criancas: "))

t1 = (((v) - (v * 0.1))*n)
t2 = (((v) - (v * 0.3))*n)
t3 = (((v) - (v * 0.4))*n)


if(n == 1):
	print(t1)
elif(n == 2):
	print(t2)
elif(n >= 3):
	print(t3)