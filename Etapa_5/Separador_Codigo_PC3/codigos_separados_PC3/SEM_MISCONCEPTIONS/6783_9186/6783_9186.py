nascimento = int(input("Digite o ano :"))
pais = input( "Digite B ou E : " )
min_br = 18
min_eua = 16
ano_cons = 2023
idade = ano_cons - nascimento
aptidao_br = idade - min_br
qnt_falta_br = min_br - idade
aptidao_eua = idade - min_eua
qnt_falta_eua = min_eua - idade
if ( pais == "B" and idade >= 18 ) :
	print("sim")
	print(aptidao_br) 
elif ( pais == "B" and idade < 18):
	print("nao")
	print(qnt_falta_br)
elif (pais == "E" and idade >= 16) :
	print("sim")
	print(aptidao_eua)
elif ( pais == "E" and idade < 16) :
	print("nao")
	print(qnt_falta_eua)
else:
	print("invalido")
	
	