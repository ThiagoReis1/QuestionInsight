c= float(input("Quantidade de combustivel comum: "))

if(c< 17.5):
	v= c+1.5
	print(round(v,2))
elif(c>17.5)and (c<35):
	v= c+2.3
	print(round(v,2))
elif(c>35) and (c<50):
	v= c+3.3
	print(round(v,2))
else:
	v=c+4.7
	print(round(v,2))