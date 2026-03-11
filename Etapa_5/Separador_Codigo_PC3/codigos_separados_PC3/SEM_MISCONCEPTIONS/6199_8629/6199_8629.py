altura_cicero = 1.8
taxa_cicero = 0.01
altura_pessoa = float(input("altura de uma pessoa:"))
taxa_crescimento_pessoa = float(input("taxa de crescimento: "))
anos = 0

while (altura_pessoa < altura_cicero):
	altura_pessoa = altura_pessoa + taxa_crescimento_pessoa
	altura_cicero = altura_cicero + taxa_cicero
	
	anos = anos + 1
	
print(anos)