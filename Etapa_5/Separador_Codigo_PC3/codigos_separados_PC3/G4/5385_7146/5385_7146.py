s = input().upper()

a = s.upper().count("A")
e = s.upper().count("E")
i = s.upper().count("I")
o = s.upper().count("O")
u = s.upper().count("U")

v = a + e + i + o + u
c = len(s) - v

pa = v * 35.15
pv = c * 42.17

soma = pa + pv

print(round(soma,2))