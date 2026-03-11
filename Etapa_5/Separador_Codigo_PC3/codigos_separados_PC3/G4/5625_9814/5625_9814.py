TS = input("escolher T ou S: ")
qtd = int(input("quantidade de comida: "))
ac = int(input("quantidade de acai: "))

pac = ac * 10
pt = qtd * 5.50
ps = qtd * 4.00

if TS == "T" :
	print(round(pt + pac, 2))
else:
	print(round(ps + pac, 2))