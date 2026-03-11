v = int(input("digite: "))

qa = 0
qb = 0
qc = 0
qv = 0

while v > qv:
	n = input("canditado: ")
	if n.lower() == "tais":
		qv = qv +1
		qa = qa +1
	elif n.lower() == "edgar":
		qv = qv + 1
		qb = qb + 1
	elif n.lower() == "ana":
		qv = qv +1
		qc = qc +1
		
print("tais=",qa)
print("edgar=",qb)
print("ana=",qc)
	
	 
	