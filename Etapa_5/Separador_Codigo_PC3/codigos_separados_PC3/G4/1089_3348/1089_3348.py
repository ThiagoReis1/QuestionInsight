a= float(input())
b= float(input())
c= float(input())
limite= float(input())
if( a + b + c <= limite):
	print(round((a + b + c),2))
	print("Nao ultrapassou")
else:
	print(round((a + b + c),2))
	print("Ultrapassou")