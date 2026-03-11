cabeca = input("Aameul ou Hethradiah: ")

D1 = float(input("digite o valor da face do primeiro dado: "))
D2 = float(input("digite o valor da face do segundo dado: "))
D3 = float(input("digite o valor da face do terceiro dado: "))
soma = D1+D2+D3
Aameul = 8+soma
Hethradiah = 2*soma



if(cabeca == Aameul):
	mensagem = 8 + soma
	
else:
	mensagem = 2 * soma
	print(mensagem)
		
	
	
	
