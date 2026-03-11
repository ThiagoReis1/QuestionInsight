n= int(input("numero: "))


d1= (n//10000)%100000
d2=(n//100)%100
d3= n%100

x= (d1**3) + (d2**3) + (d3**3)
if( n==x ):
	print("atende") 
else:
	print("nao atende")
print(n)
	
