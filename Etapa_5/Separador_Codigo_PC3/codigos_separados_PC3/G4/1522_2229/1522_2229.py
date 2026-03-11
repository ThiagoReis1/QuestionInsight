from math import*

qi=int(input("quantidade inicial: "))
dm=int(input("despesa mensal: "))
qm=int(input("moedas de ouro coletadas: "))
qr=int(input("moedas roubadas: "))
quant=qi
mes=0

while(quant>0):
	quant= quant - dm + qm -qr
	mes=mes+1
	
print(mes)