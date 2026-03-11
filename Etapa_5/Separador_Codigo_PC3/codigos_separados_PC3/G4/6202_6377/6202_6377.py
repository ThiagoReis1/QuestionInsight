ax = float (input("altura de Bia: "))  
tx= float (input("taxa de crecimento: "))

				
al= 1.69
tl=0.01
c=0
				
while(ax< al):
   ax = ax + tx
   al = al+tl
	
   c += 1
print(c)
		