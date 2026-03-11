combustivel= float(input())

if combustivel<17.5:
	total= combustivel + 10.5
	
elif 17.5<combustivel<35.0:
	total= combustivel + 14.0
	
elif 35.0<combustivel<50.0:
	total= 18.6

else: 
	total= combustivel + 24.5
	
print(round(total,2))