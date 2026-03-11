v= float(input("valor da idenizacao: "))
c= float(input("saque mensal: "))
j= float(input("taxa de juros: "))
tempo= 15
i =0
while(tempo <= 15):
		if(v > 0 and c > 0 or j < 0 ):
			mensagem = "Dados incorretos"
			tempo= tempo + 1
			i = i +1
print(round(tempo, 2))
