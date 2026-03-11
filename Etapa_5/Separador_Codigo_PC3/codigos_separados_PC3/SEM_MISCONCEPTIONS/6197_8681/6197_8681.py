altura_pessoa = float(input("Insira a altura de uma pessoa: "))
taxa_pessoa = float(input("Insira a taxa de crescimento da pessoa: "))
altura_alice = 1.6
taxa_alice = 0.02

a = 0		#variavel de tempo

while(altura_pessoa < altura_alice):
	
	altura_pessoa = altura_pessoa + taxa_pessoa
	altura_alice = altura_alice + taxa_alice
	
	a = a + 1

print(a)