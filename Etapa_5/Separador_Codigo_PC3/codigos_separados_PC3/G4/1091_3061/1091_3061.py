n=int(input("Coloque n aqui :"))
d1=(n//1000)%10
d2=(n//100)%10
d3=(n//10)%10
d4=(n//1)%10
if(n == ( (d1*10 + d2) + (d3*10 + d4) )**2 ):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")
		 
