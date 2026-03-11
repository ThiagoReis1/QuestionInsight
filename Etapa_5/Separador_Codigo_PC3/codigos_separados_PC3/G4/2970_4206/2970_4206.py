a = float(input())
i = round(((1042000/1500)**(1/a))-1,5)
print(i)
if(i<=0.01):
	print("Real")
else:
	print("Irreal")