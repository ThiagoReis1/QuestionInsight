#UNIVERSIDADE FEDERAL DO AMAZONAS
#ENGENHARIA QUIMICA
#MICHAEL EVANGELISTA DA CRUZ - 21600845
#DATA: 05/08/2016
#AVALIACAO PARCIAL 04

copinicial = int(input("No. de copias iniciais: "))
taxa = int(input("Taxa de redução semanal: "))
copintrod = int(input("No. de copias introduzidas: "))

contador = 0
soma = copinicial

while(soma <= 1000000):
	soma = (soma - (soma*taxa/100)) + copintrod
	
	contador = contador + 1
	
print(contador)