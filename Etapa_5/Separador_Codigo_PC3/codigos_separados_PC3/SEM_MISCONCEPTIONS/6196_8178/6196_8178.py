altura_chico = 1.5
taxa_chico = 0.02

altura_pessoa = float(input("digite a altura da pessoa: "))
tdc_da_pessoa = float(input("digite a taxa de crescimento da pessoa: "))

anos = 0
while altura_pessoa < altura_chico:
	altura_chico += taxa_chico
	altura_pessoa += tdc_da_pessoa
	anos += 1 
	
print(anos)