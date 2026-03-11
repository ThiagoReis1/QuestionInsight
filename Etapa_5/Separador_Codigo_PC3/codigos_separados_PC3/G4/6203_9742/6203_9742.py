al = float(input("atura: "))
tl = float(input("taxa: "))
am = 1.4
tm = 0.06
a = 0 

while am<al:
	am = am + tm
	al = al + tl
	a = a + 1
	
print(a)
