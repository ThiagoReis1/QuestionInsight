n = int(input("capacidade n"))
eo = int(input("estoque inicial"))
q = int(input("quantidade q"))
a = eo - q
viagem = 1

if(n<=q):
	while(a>0):
	
	viagem = viagem +1
