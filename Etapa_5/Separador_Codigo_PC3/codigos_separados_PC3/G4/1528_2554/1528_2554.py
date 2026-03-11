fg=int(input("Pnts de força de cada guerreiro a cada rodada: "))
ft0=int(input("a qntd de pnts de forca inicial do troll: "))
ftr=int(input("a qntd de pnts de forca recuperada do troll a cada rodada: "))
rodada=0
while(ft0!=0 and ft0>0):
	ft0=ft0-(5*fg)+ftr
	rodada = rodada + 1
print(rodada)
	