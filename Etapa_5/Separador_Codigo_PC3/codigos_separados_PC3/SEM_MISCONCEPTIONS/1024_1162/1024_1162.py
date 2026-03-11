a = float(input("qual o lado a"))
b = float(input("qual o lado b"))
c = float(input("qual o lado c"))
custo = float(input("qual o custo da construcao"))
peri = (a + b + c)
total = peri * custo
print(round(total, 2))
