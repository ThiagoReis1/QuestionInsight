
n_1 = float(input("Digite n1:"))
n_2 = float(input("Digite n2:"))
n_3 = float(input("Digite n3:"))
n_4 = float(input("Digite n4:"))
	
media = (n_1 + n_2 +n_3 + n_4)/4
				
if(media >= 5.0):
	mensagem = "Aprovacao"
	print(round(media,2))
	
	print(mensagem)
   
	
else:
	mensagem = "Reprovacao"
	print(round(media,2))
	print(mensagem)
	
	