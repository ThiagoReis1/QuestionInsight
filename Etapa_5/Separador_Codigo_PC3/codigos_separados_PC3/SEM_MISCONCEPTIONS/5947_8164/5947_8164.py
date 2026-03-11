ce = input("(C) coxinha ou (E) esfirra: ").upper()
if ce == "C":
	ce = 1
else:
   ce = 2
	
C = 2.00
E = 4.50
S = 6.00

qtce = int(input("quantidade de coxinhas ou esfirras: "))
sucos = int(input("quantidade de sucos: "))
if ce == 1:
	total1 = qtce*C+sucos*S
	print(total1)
else:
	total2 = qtce*E+sucos*S
	print(total2)
