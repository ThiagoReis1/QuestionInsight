from numpy import*
p = input("produto: ").upper()
qh = 0
qc = 0 
ql = 0 
i = 0 
while i < len(p):
	if p [i] == "H": 
		qh+= 1 
	if p [i] == "C":
		qc+=1
	if p [i] == "L":
		ql+=1
	i+=1
t = (qh*5.40)+(qc*8.95)+(ql*4.50)
print(round(t,2))
print(qh)
print(qc)
print(ql)