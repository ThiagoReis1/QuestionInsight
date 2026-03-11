LP= input("inserir item: ").upper()
QLP= int(input("inserir quantidade: "))
QR= int(input("inserir quantidade: "))

L= 6.00
P= 4.50
R= 3.0

if (LP == "L"):
	PF= QLP*(L) + QR*(R)
else:
	PF= QLP*(L) + QR*(R)
print(PF, 2)
