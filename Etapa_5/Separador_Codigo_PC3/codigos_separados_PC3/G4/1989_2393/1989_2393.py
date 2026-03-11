info=input()
if(info=="ASPARAGINA"):
	print(round(4*12.011+8*1.00794+2*14.00674+3*15.999,2))
elif(info=="GLUTAMINA"):
	print(round(5*12.011+8*1.00794+1*14.00674+4*15.999,2))
elif(info=="TRIPTOFANO"):
	print(round(11*12.011+11*1.00794+2*14.00674+2*15.999,2))
else:
	print("Entrada:",info)
	print("Dado Invalido")