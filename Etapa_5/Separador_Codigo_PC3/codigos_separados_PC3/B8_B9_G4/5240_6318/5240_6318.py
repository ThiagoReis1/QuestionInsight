c= int(input())

if(c<100):
	t = 50+c*0.50
	print(round(t,2))
elif(c>=100  and c<250):
	t = 50+0.75*c
	print(round(t,2))
elif(c>=250 and c<500):
	t = 50+1.00*c
	print(round(t,2))
elif(c>=500):
	t = 50+1.25*c
	print(round(t,2))



