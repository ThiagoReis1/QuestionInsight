p = input("digite os produtos: ").upper()
c = 0
v = 0
while c < len(p):
   if p[c] == "A":
      v += 19.9
   elif p[c] == "L":
      v += 3.5
   elif p[c] == "P":
      v += 4.25
   c += 1
print(round(v,2))