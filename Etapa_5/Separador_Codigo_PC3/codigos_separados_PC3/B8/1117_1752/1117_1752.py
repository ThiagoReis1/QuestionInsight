preco_entrada=float(input("Informe preço da entrada: "))
dia_da_semana=int(input("Informe dia da semana: "))
musica_ao_vivo=input("Digite S para sim e N para nao")
if(preco_entrada<0) and (dia_da_semana>7 or dia_da_semana<1) and (musica_ao_vivo!=S or musica_ao_vivo!=N):
	print("Entradas:", preco_entrada, dia_da_semana, musica_ao_vivo)
	print("Dados invalidos")
elif((dia_da_semana%7==3 or dia_da_semana%7==2 or dia_da_semana%7==5) and (musica_ao_vivo==S)):
	preco=(preco_entrada+20)*(25/100)
	print("Entradas:", preco_entrada, dia_da_semana, musica_ao_vivo)
	print("Valor a pagar: R$", round(preco, 2))
elif(dia_da_semana%7!=3 or dia_da_semana%7!=2 or dia_da_semana%7!=5) and (musica_ao_vivo==S):
	preco=(preco_entrada+20)
	print("Entradas:", preco_entrada, dia_da_semana, musica_ao_vivo)
	print("Valor a pagar: R$", round(preco, 2))
elif(dia_da_semana%7!=3 or dia_da_semana%7!=2 or dia_da_semana%7!=5) and (musica_ao_vivo!=N):
	preco=preco_entrada
	print("Entradas:", preco_entrada, dia_da_semana, musica_ao_vivo)
	print("Valor a pagar: R$", round(preco, 2))
elif((dia_da_semana%7==3 or dia_da_semana%7==2 or dia_da_semana%7==5) and (musica_ao_vivo==N)):
	preco=(preco_entrada*(25/100))
	print("Entradas:", preco_entrada, dia_da_semana, musica_ao_vivo)
	print("Valor a pegar: R$", round(preco, 2))