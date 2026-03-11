#Universidade Federal do Amazonas
#Exerc. Avaliativo Olímpico
#Pedro Vinícius Borges de Souza - 21650221
#Engenharia Química

#####################################################

tamb = int(input("Digite a população inicial de tambaquis: "))
pac = int(input("Digite a população inicial de pacus: "))
tax1 = int(input("Digite a taxa de crescimento mensal do Tambaqui: "))
tax2 = int(input("Digite a taxa de crescimento mensal do Pacu: "))
n = int(input("Numero maximo de espécies comportadas no viveiro: "))
a = 0

while (tamb+pac) <= n:
	rt = tamb * (tax1/100)
	rp = pac * (tax2/100)
	tamb = tamb + rt 
	pac = pac + rp
	a = a + 1
print(a)