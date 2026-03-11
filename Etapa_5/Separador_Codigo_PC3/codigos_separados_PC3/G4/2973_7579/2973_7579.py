#programa velocidade 
s = float(input(":"))
v = float(input(":"))
t = float(input(":"))


sf = s +(v * t)

if v <= 100:
	print(int(sf))
	print("OK")
	
else:
	print(int(sf))
	print("ACIMA")