vol_inicial = int(input("Volume inicial da masmorra: "))
vazao = int(input("Volume de água que entra na masmorra por minuto: "))
evasao = int(input("Volume de água que a elfa tira por minuto: "))

volume = vol_inicial 
minutos = 0

while volume > 1000:
	volume = volume + vazao - evasao
	minutos = minutos + 1
	
print (minutos)