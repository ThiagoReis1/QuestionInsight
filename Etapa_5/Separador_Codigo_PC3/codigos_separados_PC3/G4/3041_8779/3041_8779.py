x= float(input())
if -1000<=x<-2:
	f= -1/(x+2)
	print(round(f, 4))
elif 2<x<=1000:
	f= 1/(x-2)
	print(round(f, 4))
else:
	print('entrada invalida')