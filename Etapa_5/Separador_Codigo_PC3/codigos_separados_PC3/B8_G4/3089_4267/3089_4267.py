mov = 1
soma = 0
while(mov!=0):
	mov = int(input("Digite o movimento: "))
	soma = soma + mov

if(soma<0):
	print(soma)
	print("Esquerda")
else:
	if(soma>0):
		print(soma)
		print("Direita")
	else:
		if(soma==0):
			print(soma)
			print("Inicial")

	