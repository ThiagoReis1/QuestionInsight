altura_chico = 1.5
crescimento_chico = 0.02
altura_pessoa = float(input())
crescimento_pessoa = float(input())
anos = 0 

while altura_pessoa < altura_chico:
	altura_pessoa = altura_pessoa + crescimento_pessoa 
	altura_chico = altura_chico + crescimento_chico
	anos = anos + 1
	
print(anos)