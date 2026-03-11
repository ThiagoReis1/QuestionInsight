cid = input()
ida = int(input())

n1 = "Porto Velho"
n2 = "Santarem"
n3 = "Belem"
n4 = "Tefe"
n5 = "Tabatinga"

print("Entradas: ",cid, ",", ida)

if (cid == n1 or cid == n2 or cid == n3 or cid == n4 or cid == n5) and (ida > 0 and ida < 150):
	if cid == n1:
		if ida <= 2:
			print("Passagem: R$", 0)
		elif 3 <= ida <= 12:
			total = 500/2
			print("Passagem: R$", round(total,2))
		elif 12 < ida < 65:
			total = 500
			print("Passagem: R$", round(total,2))
		elif ida >= 65:
			total = 500 - (500*0.30)
			print("Passagem: R$", round(total,2))
	if cid == n2:
		if ida <= 2:
			print("Passagem: R$", 0)
		elif 3 <= ida <=12:
			total = 370/2
			print("Passagem: R$", round(total,2))
		elif 12 < ida < 65:
			total = 370
			print("Passagem: R$", round(total,2))
		elif ida >= 65:
			total = 370 - (370*0.30)
			print("Passagem: R$", round(total,2))
	if cid == n3:
		if ida <= 2:
			print("Passagem: R$", round(total,2))
		elif 3<= ida <= 12:
			total = 600/2
			print("Passagem: R$", round(total,2))
		elif 12< ida < 65:
			total = 370
			print("Passagem: R$", round(total,2))
		elif ida >= 65:
			total = 600 - (600*0.30)
			print("Passagem: R$", round(total,2))
	if cid == n4:
		if ida <= 2:
			print("Passagem: R$", 0)
		elif 3<= ida <=12:
			total = 360/2
			print("Passagem: R$", round(total,2))
		elif 12 < ida < 65:
			total = 360
			print("Passagem: R$", round(total,2))
		elif ida >= 65:
			total = 360 - (360*0.30)
			print("Passagem: R$", round(total,2))
	if cid == n5:
		if ida <= 2:
			print("Passagem: R$", 0)
		elif 3 <= ida <= 12:
			total= 550/2
			print("Passagem: R$", round(total,2))
		elif 12 < ida < 65:
			total = 550
			print("Passagem: R$", round(total,2))
		elif ida >= 65:
			total = 550 - (550*0.30)
			print("Passagem: R$", round(total,2))
else:
	print("entradas invalidas")