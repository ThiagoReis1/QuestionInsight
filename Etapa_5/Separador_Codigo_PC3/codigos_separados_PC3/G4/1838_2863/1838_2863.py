r1 = float(input("Resistor 1: "))
r2 = float(input("Resistor 2: "))
r3 = float(input("Resistor 3: "))

req = (r1*r2*r3)/((r1*r2) + (r2*r3) + (r1*r3))
						
print(req)