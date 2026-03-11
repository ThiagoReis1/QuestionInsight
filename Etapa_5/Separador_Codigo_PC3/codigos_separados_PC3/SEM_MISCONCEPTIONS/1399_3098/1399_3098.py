votosa= float(input("votos para Ambrosio Rutra"))
votosd= float(input("votos para Demelza Olecram"))
#votosa + votosd = 100%
#votosa =x(porcentagem de a)
#porcentagem de a= (1/100*votosa)/(votosa+votod)
porce_a=((votosa)/(votosa+votosd))*100
porce_d=((votosd)/(votosa+votosd))*100
if(porce_a>porce_d):
	print("Ambrosio Rutra")
	print(round(porce_a,2))
else:
	print ("Demelza Olecram")
	print(round(porce_d,2))
