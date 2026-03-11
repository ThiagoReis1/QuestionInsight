from numpy import*

v = array(eval(input("Vet.Nume: ")))

i = 0
x = 200
y = 0
while  y < x:
	if size(v) == 6:
		x = x * 3
		y = x
	elif size(v) == 5:
		x = x / 2
		y = x
	elif size(v) == 4:
		x = x * 3
		y = x
	elif size(v) == 3:
		x = x / 2
		y = x
	elif size(v) == 2:
		x = x * 3
		y = x
	elif size(v) == 1:
		x = x / 2
		y = x
	i = i + 1
	
print (x)
print(y)
		
		
		