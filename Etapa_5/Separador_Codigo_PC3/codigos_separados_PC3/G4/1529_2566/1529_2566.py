qi = int(input("Quantidade inicial de guerreiros na infantaria: "))
qv = int(input("Quantidade inicial de guerreiros na cavalaria: "))
pi = float(input("Percentual mensal de crescimento da tropa de infantaria: "))
pv = float(input("Percentual mensal de crescimento da tropa de cavalaria: "))

meses = 0
qt = qi + qv

while (qt == 50000):
	qi = qi + (qi*pi/100)
	qv = qv + (qv*pv/100)
	meses = meses + 1	
print(meses)
