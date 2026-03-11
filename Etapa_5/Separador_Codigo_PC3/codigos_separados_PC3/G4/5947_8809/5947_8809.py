ce=input("coxinha ou esfirra: ")
qce=int(input("quantidade de coxinha ou esfirra: "))
qc=int(input("quantidade de suco: "))
if ce.upper() == "C":
	ct=(2.00*qce)+(qc*6.00)
	print(round(ct,2))
else:
	ct2=(4.50*qce)+(qc*6.00)
	print(round(ct2,2))