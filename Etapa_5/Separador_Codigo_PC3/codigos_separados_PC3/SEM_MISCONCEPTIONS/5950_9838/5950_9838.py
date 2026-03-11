op = (input("Digite T se for fatia de torta ou P se for pastel: "))
qntTouP = int(input("Qual a quantidade de fatias de torta ou pasteis? "))
qntcap = int(input("Qual a quantidade de cappuccinos? "))

torta = 6
pastel = 5
capp = 4.5

if op.upper() == "T":
	tot = qntTouP*torta + qntcap*capp
else:
	tot = qntTouP*pastel + qntcap*capp
	
print(round(tot,2))