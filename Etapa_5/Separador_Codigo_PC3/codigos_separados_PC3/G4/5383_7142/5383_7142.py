s = input().upper()

a = s.upper().count("A")
e = s.upper().count("E")
i = s.upper().count("I")
o = s.upper().count("O")
u = s.upper().count("U")

v = a+e+i+o+u
c = len(s)-v

pa = v * 0.12
pc = c * 0.18

soma = pa+pc

print(round(soma,2))
