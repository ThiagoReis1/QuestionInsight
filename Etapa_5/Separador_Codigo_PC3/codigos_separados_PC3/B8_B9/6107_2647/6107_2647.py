entrada = int(input())

if(entrada<17.5):
	print(round((entrada+1.5),2))
elif(entrada<35):
	print(round((entrada+2.3),2))
elif(entrada<50):
	print(round((entrada+3.3),2))
elif(entrada>=50):
	print(round((entrada+4.7),2))