merenda=input("digite s ou b= ").upper()
bols=int(input("quantidades de fatias de bolo ou salgado= "))
cap=int(input("quantidade de cappucino= "))

if merenda == "B":
	total=(bols*5) + (cap * 7.50)
	print(total)
if merenda == "S":
	total=(bols * 4) + (cap * 7.50)
	print(total)

