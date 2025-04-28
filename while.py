#stock limit
stock = 10

#number of purchases
num_purchases = 0

while num_purchases < stock:
    num_purchases +=1
    if stock - num_purchases > 7:
        print("plenty of stock")
    elif stock - num_purchases > 3:
        print("some stock")
    elif stock - num_purchases !=0:
        print("low stock")
    else:
        print("no stock")
    

tickets_sold = 0 
max_capacity = 10

while tickets_sold < max_capacity:
    tickets_sold +=1
print("sold out:", tickets_sold, "tickets sold")


release_date =26
current_date = 22
while current_date <= release_date:
    if current_date <= 24:
        print("pruchase before 25th for earl access")
    elif current_date == 25:
        print("coming soon")
    else:
        print("available now")
   
    current_date +=1

