x = float(input())

kg = 43.21
taxa = 25.0
icms = 100/62

val = ((x*kg) + taxa)
a = (val/100) * 62  # cal icms
formula = val + a

print(round(formula, 2))