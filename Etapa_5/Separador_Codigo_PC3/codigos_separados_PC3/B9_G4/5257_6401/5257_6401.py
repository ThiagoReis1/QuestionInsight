c = float(input("Custo do produto: "))

if(c <= 50):
	l = c * 2
	
elif(c > 50) and (c < 100):
	l = c + (c / 2)

elif(c > 100) and (c < 500):
	l = c + (c * 0.4)
	
else:
	l = c + (c * 0.3)
	
print(round(l, 2))