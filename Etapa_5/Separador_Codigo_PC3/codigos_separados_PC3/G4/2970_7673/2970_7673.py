t = float(input())
Qf = 1042000  
Qo = 1500

i = ((Qf / Qo) ** (1 / t)) - 1

if(i <= 0.01):
	print(round(i, 5))
	print("Real")
else:
	print(round(i , 5))
	print("Irreal")