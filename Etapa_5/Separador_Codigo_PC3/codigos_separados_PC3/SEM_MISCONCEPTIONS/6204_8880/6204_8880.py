altura= float(input("altura: "))
tc= float(input("taxa de crescimento: "))
alturamacaco = 1.86
taxamacaco = 0.01
anos =0

while (alturamacaco>altura):
	altura= altura+tc 
	alturamacaco= taxamacaco + alturamacaco
	anos=anos+1
print(anos)
	
	
	
