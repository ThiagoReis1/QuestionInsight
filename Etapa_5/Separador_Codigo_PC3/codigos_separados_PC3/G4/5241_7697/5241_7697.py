a=float(input("numero:"))
if(a>0):
	if(a<10):
		b=a*2+20.00
		print(round(b,2))
	elif((a<=10)or(a<20)):
		
			c=a*2.5+20.00
			print(round(c,2))
	elif ((a<=20)or(a<40)):
		
			d=a*2.75+20.00
			print(round(d,2))
	elif((a>40)):
		
			e=a*3.0+20.00
			print(round(e,2))
	
	else:
		print("dados invalidos")
	
  