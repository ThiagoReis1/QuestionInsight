sal = input ("digite C para coxinha ou E para esfirra: ").upper()
qua = int (input ( "digite quantos salgados: "))
suc = int ( input ( "digite quantos sucos:"))

if sal == "C":
	total = qua * 2 + suc * 6
	print (round (total, 1))
	
else:
	total = qua * 4.5 + suc * 6
	print (round (total, 2))