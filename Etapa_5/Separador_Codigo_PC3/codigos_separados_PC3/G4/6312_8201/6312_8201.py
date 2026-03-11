e=input().upper()
i=0
qb=0
qc=0
qe=0
while i<len(e):
	if e[i]=="B":
		qb+=1
	if e[i]=="C":
		qc+=1
	if e[i]=="E":
		qe+=1
	i+=1
t=round((qb*3.75+qc*7.90+qe*9.85), 2)
print(t, qb, qc, qe)

	