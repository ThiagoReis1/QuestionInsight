P = float(input("peso"))
CF = 10.00

if P < 5:
	TA = 3.75
	PF = TA+ CF
	print(round(PF,2))
elif P == 5:
	TA = 4.75
	PF = TA+CF
	print(round(PF,2))
elif P > 5 :
	TA = 5.75
	PF = TA+CF
	print(round(PF,2))