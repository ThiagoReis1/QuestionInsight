x = int(input('valor inferior: '))
y = int(input('valor superior: '))
ctd = 0
while x <= y:
  if x % 7 == 0:
    ctd = ctd + x
  x += 1
print(ctd)