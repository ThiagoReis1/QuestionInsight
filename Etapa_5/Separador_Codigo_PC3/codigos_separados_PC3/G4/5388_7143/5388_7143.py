x = input(("").upper())

a = x.upper().count("A")
e = x.upper().count("E")
i = x.upper().count("I")
o = x.upper().count("O")
u = x.upper(). count("U")

v = a+e+i+o+u
c = len(x)-v

pa = v * 25.12
pc = c * 40.18

soma = pc+pa

print(round(soma,2))