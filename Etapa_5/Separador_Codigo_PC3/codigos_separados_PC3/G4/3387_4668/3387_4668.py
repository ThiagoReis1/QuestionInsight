medida=input("M ou K:")
qnt=float(input("quantidade:"))
if(medida=="K"):
	mg=2.35215*qnt
	print(round(mg,2))
else:
	kl=qnt/2.35215
	print(round(kl,2))