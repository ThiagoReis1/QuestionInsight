a = int(input())
b = int(input())
c = int(input())

ad = a % 2
bd = b % 2
cd = c % 2

if (ad == 0 and bd == 0 and cd == 0):
	
	print ("SIM")
	
elif ((ad == 0 and bd == 0) or (bd == 0 and cd == 0) or (ad == 0 and cd == 0)):
	
	print ("SIM")
	
else:
	
	print ("NAO")
	