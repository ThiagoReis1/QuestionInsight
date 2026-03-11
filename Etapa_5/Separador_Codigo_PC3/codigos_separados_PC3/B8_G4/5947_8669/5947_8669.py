esc= input("C ou E: ")
qts= int(input("quantos? "))
suco= int(input("sucos?"))

if esc.upper() == "C":
	total= (qts * 2)+(suco * 6)
	print(round(total,1))

elif esc.upper() == "E":
	total= (qts * 4.5)+(suco * 6)
	print(round(total,1))