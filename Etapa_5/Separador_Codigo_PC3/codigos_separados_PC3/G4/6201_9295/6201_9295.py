a_p = float(input("Insira a altura: "))
t_p = float(input("Insira a taxa de crescimento: "))
a_j = 1.77
t_j = 0.02
cont = 0

while (a_p < a_j):
	a_p = a_p * t_p
	a_j = a_j * t_j
	cont = cont + 1
	
	print(cont)

	