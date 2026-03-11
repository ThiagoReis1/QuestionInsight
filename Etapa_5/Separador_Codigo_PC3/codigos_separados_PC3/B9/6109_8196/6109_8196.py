var1 = int(input("leia a quantidade de combustivel comum: "))

if(var1 < 17.5):
	result = var1 + 1.5
elif(var1 >= 17.5 and var1 < 35):
   result = var1 + 2.3 
elif(var1 >= 35 and var1 < 50):
	result = var1 + 3.3
	
else:
	result = var1 + 4.7

print(round(result,2))