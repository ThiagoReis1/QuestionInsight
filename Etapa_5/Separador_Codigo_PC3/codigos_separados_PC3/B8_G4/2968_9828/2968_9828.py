c = input("L ou S: ")
qc = int(input("Qtd L ou S: "))
r = int(input("R: "))
tl = qc*5 + r*4
ts = qc*3.5 + r*4

if  c == "L":
		print(tl)
elif c == "S":
		print(ts)