altp = float(input("altura pessoa: "))
taxp = float(input("taxa pessoa: "))

altc = 1.8
taxc = 0.01
ano = 0

while altp < altc:
	altp = altp + taxp
	altc = altc + taxc
	ano = ano + 1
	
print(ano)	