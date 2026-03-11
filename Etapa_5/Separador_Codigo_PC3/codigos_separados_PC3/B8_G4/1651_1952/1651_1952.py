#Lucas Nascimento Estevam da Silva		21602757
#Trabalho Pratico 06
#Exercicio 02

from numpy import*

tom = input("Tons: ")
mc = 0
c = 0
cm = 0
em = 0
e = 0
me = 0

vet = zeros(6, dtype = int)
for i in range(size(tom)):
	if(tom[i] == 'MC'):
		mc = mc + 1
		
	elif(tom[i] == 'C'):
		c = c + 1
		
	elif(tom[i] == 'CM'):
		cm = cm + 1
		
	elif(tom[i] == 'EM'):
		em = em + 1
		
	elif(tom[i] == 'E'):
		e = e + 1
		
	elif(tom[i] == 'ME'):
		me = me + 1
		
vet[0] = mc
vet[1] = c
vet[2] = cm
vet[3] = em
vet[4] = e
vet[5] = me

print(max(vet))
print(vet)