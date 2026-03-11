altura_macaco = 1.4
taxa_macaco = 0.06

altura_leao = float(input("altura inicial do leao: "))
taxa_leao = float(input("taxa de crescimento do leao: "))

ano = 0 

while altura_macaco <+ altura_leao:
	altura_macaco += taxa_macaco
	altura_leao += taxa_leao
	ano += 1
	
print(ano)
