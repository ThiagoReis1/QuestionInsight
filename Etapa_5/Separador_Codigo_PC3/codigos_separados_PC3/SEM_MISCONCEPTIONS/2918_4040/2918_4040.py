#Insertable data

price_of_the_tickets = float(input("Price of the Tickets: "))
amount_of_tickets = int(input("Amount of bought tickets: "))

#Computation

total_price = (amount_of_tickets)*(0.8*(price_of_the_tickets))
print(round(total_price,2))