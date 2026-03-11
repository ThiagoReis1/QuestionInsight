c = 2
e = 4.5
s = 6

escolha = input("Digite C para coxinha e E para esfirra: ")
quantidade = int(input("Escreva a quantidade de coxinhas ou esfirras: "))
quantidadesuco = int(input("Escreva a quantidade de sucos: "))

if(escolha == "C"):
	soma = c*quantidade + s*quantidadesuco
	print(soma)
elif(escolha == "E"):
	soma = e*quantidade + s*quantidadesuco
	print(soma)