# Ariane Medeiros
# Lab1 Ex1
# 30 - 06 - 2016

bra = float(input('Digite o valor de compra a:'))
brb = float(input('Digite o valor de compra b:'))
brc = float(input('Digite o valor de compra c:'))
brd = float(input('Digite o valor de compra d:'))
bre = float(input('Digite o valor de compra d:'))


valortotal = (bra+brb+brc+brd+bre)

if(valortotal <= bra+brb+brc+brd+bre):
	mensagem = "Sim"

else:
	mensagem = "Nao"


print(round(valortotal - bra+brb+brc+brd+bre,2))	
print(mensagem)
	
