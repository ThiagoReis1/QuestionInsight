#Quantidade inicial
QI = int(input())
#Despesa mensal
DM = int(input())
#Moedas coletadas em impostos
QM = int(input())
#Moedas roubadas
QR = int(input())

t = 0

while(QI > 0):
	QI = QI + QM - DM - QR
	t = t + 1
print(t)