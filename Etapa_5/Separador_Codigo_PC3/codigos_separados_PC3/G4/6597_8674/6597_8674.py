# faça seu código aqui!
N = int(input("quantidade de funcionarios = "))
i = 0
a = 0
b = 0 
c = 0
while i < N:
	escolha = input().upper()
	if escolha == 'A':
		a = a + 1
	if escolha == 'B':
		b = b + 1
	if escolha == 'C':
		c = c + 1
	i = i + 1 
	
print("A=", a)
print("B=", b)
print("C=", c)
