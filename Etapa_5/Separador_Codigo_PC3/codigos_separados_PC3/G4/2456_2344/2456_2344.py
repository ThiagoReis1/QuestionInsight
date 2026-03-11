m= float(input("Digite o valor da mensalidade: "))
n= float(input("Digite a quantidade de criancas: "))


if (n == 1):
	des= 10 / 100
	V= (m -  (m * des))  * n
	print(round(V, 2))
elif (n == 2):
	des= 30 / 100
	V= (m -  (m * des))  * n
	print(round(V, 2))
else:
	des= 40 / 100
	V= (m -  (m * des))  * n
	print(round(V, 2))