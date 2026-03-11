x= int(input("qual numero:"))
num = 0
nume=0
while x!= 0:
	if x % 2:
		num= num + 1
	else:
		nume=nume+1
	x=int(input("qual numero:"))
	
f1= num+nume
f2= 100-((100/f1)*num)

print(round(f1,2))
print(round(f2,2))
	

	
	