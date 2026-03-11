a= float(input("quantidade de combustivel: "))

if(a < 17.5):
	y= a + 10.5
	
elif(a <= 17.5 or a<= 35):
	y= a + 14
	
elif(a <= 35 or a <=50):
	y= a + 18.6
	
elif(a >=50):
	y= a + 24.5
	
print(round(y,1))