#Universidade Federal do Amazonas 
#Laís Amorim Reis - 21602327

pop = int(input("pop inicial: "))
taxa = float(input("taxa: "))
retirada = int(input("retirada: "))
anos = 0
while(pop>0):
	pop = pop + ((taxa*pop)/100)
	pop = pop - retirada
	anos = anos+1
print(anos)