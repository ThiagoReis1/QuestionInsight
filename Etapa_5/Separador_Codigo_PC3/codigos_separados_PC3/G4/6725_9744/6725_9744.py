num = int(input())
a = float(num%23)
b = float(num//23)
if(a==0):
	print(int(b))
	print("sim")
else:
	print(int(a))
	print("nao")
	