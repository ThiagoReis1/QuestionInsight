altura_chico = 1.5
taxa_chico = 0.02

altura_outro = float(input())
taxa_outro = float(input())

anos = 0

while(altura_outro < altura_chico):
	altura_outro = altura_outro + taxa_outro
	altura_chico = altura_chico + taxa_chico
	anos = anos + 1
	
print(anos)