altura_bia = 1.69
taxa_bia = 0.01

alturap = float(input("digite: "))
taxap = float(input("digite: "))

cont = 0

while alturap < altura_bia:
	alturap = alturap + taxap
	altura_bia = altura_bia + taxa_bia
	cont = cont + 1
	
print(cont)