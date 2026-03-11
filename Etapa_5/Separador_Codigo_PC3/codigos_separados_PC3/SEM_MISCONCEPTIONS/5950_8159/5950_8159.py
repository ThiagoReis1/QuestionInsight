op=input("fatia de torta ou pastel(T ou P): ").upper()
if(op=="T"):
	quant_f=int(input("quantidade de fatias de torta: "))
	quant_c=int(input("quantidade de cappuccinos: "))
	conta=(quant_f*6)+(quant_c*4.5)
	print(conta)
else:
	quant_p=int(input("quantidade de pastel: "))
	quant_c=int(input("qunatidade de cappuccino: "))
	conta=(quant_p*5)+(quant_c*4.5)
	print(conta)