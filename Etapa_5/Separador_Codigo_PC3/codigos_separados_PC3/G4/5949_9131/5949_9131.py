a = input("B ou C: ")
b = a.upper()
q = int(input("quantidade:  "))
c = int(input("quantidade de cappuccinos:  "))

if b == "B":
   total = q * 3 + c *5.5
   print(round(total,2))
else:
   total = q * 6 + c *5.5
   print(round(total,2))	