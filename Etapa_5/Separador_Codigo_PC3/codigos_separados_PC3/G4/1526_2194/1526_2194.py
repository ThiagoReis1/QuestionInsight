a = int(input("quantidade inicial: "))
b = int(input("quantidade gasta: "))
c = int(input("quantidade recuperada: "))
k = a
j = 0 
while(k > 0):
	k = k + c - b
	j = j + 1

print(j)
	
	
	
	