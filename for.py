prices = [9.99, 8.99, 35.25, 1.50, 5.75]

#print each value in prices
for price in prices:
    if price > 10:
        print("more than 10")
    elif price < 5:
        print("less than 5")
    else:
        print(price)


username = "george_dc"

#print each character
for char in username:
    print(char)


products_dic = {"AG32":87.99, "HT91":21.50,
                "PL65":43.75, "OS31":19.99,
                "KB07":62.85, "TR48":98.00}

#loop through keys and values
for key, val in products_dic.items():
    print(key, val)

#loop through keys
for key in products_dic.keys():
    print(key)

#loop through values
for val in products_dic.values():
    print(val)



for i in range(1,6):
    print(i)


#no visits
visits = 0

#loop through 1-10
for i in range(1,11):
    visits +=1

print(visits)



user_ids = ["T42YG4KTK", "VTQ39IDQ0", "CRL11YUWX", 
            "K6Y5URXLR", "V4XCBER7V", "IOGQWC61K"]

for user_id in user_ids:
    print(user_id)


tickets_sold = 0
max_capacity = 30

for tickets in range(1,31):
    tickets_sold +=1

print("sold out:", tickets_sold, 'tickets sold')




courses = {"LLM Concepts": "AI", 
           "Introduction to Data Pipelines": "Data Engineering", 
           "AI Ethics": "AI",
           "Introduction to dbt": "Data Engineering", 
           "Writing Efficient Python Code": "Programming",
           "Introduction to Docker": "Programming"}

for key, value in courses.items():
    if value == "AI":
        print(key, "is an AI course")
    elif value == 'programming':
        print(key, "is a programming course")
    else:
        print(key, "is a data engineering course")


    


