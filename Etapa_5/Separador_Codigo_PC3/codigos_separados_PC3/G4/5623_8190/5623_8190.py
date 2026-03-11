BS=input("Bolo ou salgado ")
x=int(input("quantidade "))
y=int(input("quantidade cap"))

if(BS=="B"):
	total=(x*5)+(y*7.50)
else:
	total=(x*4)+(y*7.50)
	
print(total)