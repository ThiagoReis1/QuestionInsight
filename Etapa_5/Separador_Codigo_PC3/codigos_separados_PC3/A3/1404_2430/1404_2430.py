nome = input("Aameul ou Hethradiah: ")

D1 = float(input("digite o valor da face do primeiro dado: "))
D2 = float(input("digite o valor da face do segundo dado: "))
D3 =  float(input("digite o valor da face do terceiro dado: "))
R = D1 + D2 + D3
Aameul = 8 + R
Hethrediah = 2*R

if(nome == Aameul):
	mensagem = 8 + R
else:
	mensagem = 2*R
	print(mensagem)