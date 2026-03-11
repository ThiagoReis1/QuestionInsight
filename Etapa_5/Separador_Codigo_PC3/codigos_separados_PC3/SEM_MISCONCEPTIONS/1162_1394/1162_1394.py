saldo = float(input())
juros = 0
vgastado = float(input())
mes = 0

while(vgastado < saldo):
	saldo = saldo - (vgastado * mes)
	rendi = premio * (juros / 100)
	saldo = premio + rendi
	mes = mes + 1
	

print("Seu saldo será negativo em: ", mes, "meses")
	
	
	



