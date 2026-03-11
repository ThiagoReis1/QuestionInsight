N=int(int(input("Capacidade N do navio: ")))
est=int(input("Estoque inicial de containers do deposito: "))
Q=int(input("Quantidade de containers que chega a cada semana: "))
QC=est+Q
semana=0
while(est!=0):
	viagem=est-QC
	est=est-viagem
	semana=semana+1
print(semana)