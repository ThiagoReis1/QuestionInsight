vc=float(input("Qual o valor consumido? "))
if(vc<=300):
	print(round(vc*0.10+vc,2))
else:
	print(round(vc*0.06+vc,2))
