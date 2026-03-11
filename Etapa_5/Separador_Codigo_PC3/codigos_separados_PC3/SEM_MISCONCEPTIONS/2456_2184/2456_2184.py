vm=float(input("valor da mensalidade "))
nc=int(input("numero de criancas"))

if(nc==1):
	print(round((vm/100)*90),2))
elif(nc==2):
	print(round(((vm*2)/100)*70)),2)
elif(nc>=3):
	print(round(((vm*3)/100)*60)),2)

