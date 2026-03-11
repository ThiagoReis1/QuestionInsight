so = int(input("digite s0: "))
v = int(input("digite v: "))
t = int(input("digite t:"))

S = (s0 + (v*t))

if(S <= 100):
	msg = "OK"
else:
	msg = "ACIMA"
	
print(S)
print(msg)