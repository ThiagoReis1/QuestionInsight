var1 = int(input(": "))
cont = 0

while(var1!= -1):
	if( var1 >= 26 and var1 <= 85):
		cont = cont + 1
	
	var1 = int(input(": "))

print(cont)