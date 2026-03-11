x= int(input("6 digitos: "))

n1= (x//1000)
n2= (x)%1000

calculo= (n1+n2)**2

if(calculo==x):
	print("atende")
else:
	print("nao atende")

print(x)