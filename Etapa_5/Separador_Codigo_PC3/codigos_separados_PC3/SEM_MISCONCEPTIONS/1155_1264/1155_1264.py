n=int(input("numero de copias: "))
nl=int(input("Número inicial de leucócitos no sangue."))
taxa_n=float(input("Taxa em % de multiplicação diária do vírus: "))
taxa_l=float(input("Taxa em % de multiplicação diária dos leucócitos."))

dia=1
totalvirus=0
total_l=0

while(totalvirus >= 2*total_l):	
	totalvirus = n* taxa_n/100
	total_l= nl * taxa_l/100
	dia=dia+1
	
print(dia)
	
	
	
