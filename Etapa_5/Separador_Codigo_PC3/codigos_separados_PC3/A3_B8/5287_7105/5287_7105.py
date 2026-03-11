a = input().upper()
cara = 0
coroa = 0
total = 0
while(a!="S"):
	if(a == "CARA"):
		cara +=1
	elif(a == "COROA"):
		coroa +=1
	total += 1
	a = input().upper()
print(total)
print(round((cara/total)*100, 2))