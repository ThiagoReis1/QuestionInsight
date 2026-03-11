ce=int(input())

if(ce<100):
	ct= (ce*0.50)+50
	print(round(ct,2))
elif(ce>=100 and ce<250):
	ct= (ce*0.75)+50
	print(round(ct,2))
elif(ce>=250 and ce<500):
	ct= (ce*1.00)+50
	print(round(ct,2))
elif(ce>=500):
	ct= (ce*1.25)+50
	print(round(ct,2))