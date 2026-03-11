#Entradas
bolinha = input("Qual bolinha?: ")

#Variavel acumuladora
bolinha_preta = 0

a = "preta"
b = "vermelha"
c = "s"

#laço 1:
if (bolinha == a):
	while (bolinha != c):
		bolinha_preta = bolinha_preta + 1
		bolinha = input("Qual bolinha?: ")
else: 
	bolinha_preta = bolinha_preta - 1
print(bolinha_preta)



		


		
	
	