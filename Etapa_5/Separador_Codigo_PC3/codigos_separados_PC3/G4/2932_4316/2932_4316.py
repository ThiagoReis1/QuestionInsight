r1 = int(input("Digite um valor: "))
r2 = int(input("Digite outro valor: "))
r3 = int(input("Digite outro valor: "))

req1 = r1*r2*r3
req2 = (r1*r2) + (r2*r3) + (r1*r3)
req = req1/req2

print(req)