p=float(input())
c=int(input())
BF= 40/100

if(c==1):
	v=(p-p*BF) + p*(10/100)
	print(round(v,2))
elif(c==2):
	v=(p-p*BF) + p*(8/100)
	print(round(v,2))
elif(c==3):
	v=(p-p*BF)
	print(round(v,2))
elif(c==4):
	v=(p-p*BF) + p*(2/100)
	print(round(v,2))