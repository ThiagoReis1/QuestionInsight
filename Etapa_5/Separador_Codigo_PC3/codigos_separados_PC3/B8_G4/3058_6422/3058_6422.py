from math import*
a = float(input("area a ser coberta: "))



if(a>0 and a<=100):
	c = 2
	f = 100
	#print(round(v,2))
	
elif(a >=100 and a <= 2500):
   c = 1.80
   f = 150
   #print(round(v,2))
	
elif(a>=2500 and a <= 10000):
   c = 1.50
   f = 200
	#print(round(v,2))
	
elif(a > 10000):
	c = 1.20
	f = 250
	#print(round(v,2))

v = (a*c)+f
print(round(v,2))
	
#else:
	#print("entrada invalida")