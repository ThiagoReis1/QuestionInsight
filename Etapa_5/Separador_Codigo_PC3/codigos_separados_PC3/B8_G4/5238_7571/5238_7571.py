a= int(input("digite o numero: "))
b= int(input("digite o numero: "))
c= int(input("digite o numero: "))

if(a>=1000 and b>=1000 or b>=1000 and c>=1000 or c>=1000 and a>=1000 or a==1000 and b==1000 and c==1000):
	print("SIM")
elif(a<1000 and b<1000 and c<1000 or a<1000 and b<1000 or b<1000 and c<1000 or a<1000 and c<1000):
	print("NAO")
