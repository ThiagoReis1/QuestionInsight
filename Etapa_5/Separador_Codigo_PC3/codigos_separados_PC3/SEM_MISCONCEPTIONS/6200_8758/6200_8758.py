altura_max = 1.75
taxa_max = 0.01

alg = float(input("altura da pessoa: "))
cr_alg = float(input("digite os anos: ")) 

anos = 0 

while (altura_max > alg):
	altura_max = altura_max + taxa_max
	alg = alg + cr_alg 
	anos = anos + 1
	
print(anos)