i= int(input(""))
N= int(input(""))

cont= 0

while(cont<N):
	cont= cont + 1
	i= i - (5*i/100)
	
	print(round(i, 2))
