bravo = int(input("número de habitantes de bravo:"))
pentos = int(input("número de habitantes de pentos:"))
porto = int(input("número de habitantes de porto:"))
taxabravo = float(input("taxa anual de crescimento da população de bravos:"))
taxapentos = float(input("taxa anual de crescimento da população de pentos:"))
taxaporto = float(input("taxa anual de crescimento da população de porto:"))
anos = 0

while(bravo + pentos < porto):
	bravo = bravo + (bravo * taxabravo/100)
	pentos = pentos + (pentos * taxapentos/100)
	porto = porto + (porto * taxaporto/100)
	anos = anos + 1
print(anos)	