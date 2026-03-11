#Universidade Federal do Amazonas-UFAM
#aluna:  Ingrid de Lira Lima
#matricula: 21456913
#data: 30/06/2016

n1 = float(input("digite n1:"))
n2 = float(input("digite n2:"))
n3 = float(input("digite n3"))
media= (n1 + n2 + n3)/3

if(media >= 6):
	mensagem = "Aprovacao"
else:
	mensagem ="Reprovacao"
	
print(round(media,2))
print(mensagem)