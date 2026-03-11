from math import*

p = float(input("Peso espada gramas: "))

flaw = float(2**(1 + (p/1000)))

soul = p * ((pi**2)/3141)

 
oleo = 2 * (sqrt(p/40))

print(round(flaw,2))
print(round(soul,2))
print(round(oleo,2))


