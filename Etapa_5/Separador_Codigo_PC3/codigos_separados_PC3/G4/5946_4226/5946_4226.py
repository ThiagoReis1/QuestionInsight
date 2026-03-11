r = input("pedido ")
q = int(input("q. "))
s = int(input("refri "))

if r.upper() == "L":
	v = round( (q*6) + (s*3) ,2)
else:
	v = round( (q*4.5) + (s*3) ,2)

print(v)