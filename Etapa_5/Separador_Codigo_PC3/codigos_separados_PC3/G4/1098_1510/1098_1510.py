#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior
#lab de codificação 02 - Avaliação Parcial
#06.07.2016
#Solicitar número do usuário
vlr = int(input("Digite um número: "))
#Fornecer a estrutura para condição
prt1 = vlr // 1000 #primeiros algarismos
prt2 = vlr % 1000 #ultimos algarismos
#Estabelecer condição
if(vlr == (prt1 - prt2)**4):
	print(vlr, "atende a propriedade")
else:
	vlr = (prt1 - prt2)**4
	print(vlr)


