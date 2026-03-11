a = int(input())
b = input("(B) para brasil e (E) para EUA")
x = 2023-a
if(b=="B"):
	if(x>18):
		print("sim")
		apto = x-18
		print(apto)
	
	else:
		print("nao")
		apto = 18-x
		print(apto)
		
if(b=="E"):
	
	if(x>16):
		print("sim")
		apto = 18-x
		print(apto)
		
	else:
		print("nao")
		apto = 18-x
		print(apto)

	