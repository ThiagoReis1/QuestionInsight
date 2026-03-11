N = int(input("qual o numero:"))
if N >= 1:
	if (N%3==0) and (N%5==0):
		print("AuauMiau")
	elif N%3==0:
		print("Auau")
	elif N%5==0:
		print("Miau")
	else:
		print(N)
	
  