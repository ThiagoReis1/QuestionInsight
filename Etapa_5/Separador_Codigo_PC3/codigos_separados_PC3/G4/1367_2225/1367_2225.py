a= 0.31
b= 0.73
c= 2.64
qa= float(input("qa: "))
qb= float(input("qb: "))
qc= float(input("qc: "))
x= qa/a
y= qb/b
z= qc/c
qm= int(min(x,y,z))
print(qm)