kg = float(input("valor do peso: "))
tf = 25.00
qm = 43.21
icms = 62/100

total = (kg*qm)+tf
imposto = icms*total
fn = total+imposto



print (round(fn ,2))





