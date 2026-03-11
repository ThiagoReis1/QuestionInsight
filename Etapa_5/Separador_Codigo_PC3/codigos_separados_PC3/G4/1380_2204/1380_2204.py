x = float(input("estimativa de carros : "))
B = float(input("comprimento da base maior : "))
b = float(input("comprimento da base menor : "))
h = float(input("comprimento da altura : "))
formula = (B + b) * h // 2 
print(int(formula * x ))