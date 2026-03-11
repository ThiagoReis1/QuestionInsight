n = int(input("numero de bacterias:"))
taxa = int(input("taxa de crescimento:"))
q = n 
i = 0 
while q < 2*n:
	q +=(taxa/(100))*q 
	i += 1
print(i)


