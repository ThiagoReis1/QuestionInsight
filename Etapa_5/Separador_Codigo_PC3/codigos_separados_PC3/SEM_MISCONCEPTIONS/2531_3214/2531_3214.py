V=float(input("Digite o valor do premio:"))
M=float(input("Digite o valor do saque mensal fixo "))
i=float(input("Digite a taxa de juros:"))
V=round(V, 2)
while(V>0 and M>0 and i>0):
		if (V==V+(V*i/100)):
		mensagem=V
   else:
		mensagem="Dados invalidos"
	print(mensagem)	
		

		
	
		
		
		
		
		
		
		
		