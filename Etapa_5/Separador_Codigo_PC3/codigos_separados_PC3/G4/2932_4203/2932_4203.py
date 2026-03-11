r1 = int(input("quanto vale r1?"))
r2 = int(input("quanto vale r2?"))
r3 = int(input("quanto vale r3?"))

req1 = r1*r2*r3
req2 = (r1*r2) + (r2*r3) + (r1*r3)

reqt = (req1/req2)

print(reqt)