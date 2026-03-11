from numpy import*
number = array(eval(input("")))
i = 0
pont_tot = 0
pont = 80
while(i < size(number)):
	if(number[i] == 1):
		pont_tot = pont_tot + 80
	elif(number[i] == 2):
		pont_tot = pont_tot + 40
	elif(number[i] == 3):
		pont_tot = pont_tot + 20
	elif(number[i] == 4):
		pont_tot = pont_tot + 10
	i+=1
print(pont_tot)