v=int(input("Digite a velocidade:"))
t=int(input("Digite o tempo de viagem:"))
d=v*t
if d==100:
	proxima_parada= "Próxima parada:Bravos"
elif d==200:
	proxima_parada= "Próxima parada:Castamere"
elif d==400:
	proxima_parada= "Próxima parada:Doriath"
elif d==600:
	proxima_parada= "Próxima parada:Edoras"
elif d==750:
	proxima_parada= "Próxima parada:Fangorn"
elif d==1150:
	proxima_parada= "Próxima parada: Gondor"
elif d>=1400:
	proxima_parada= "Próxima parada: Hogosmead"
else:
	proxima_parada="Valor inválido"
print (proxima_parada)
