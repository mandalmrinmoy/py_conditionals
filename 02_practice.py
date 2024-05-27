# Movie tickets are priced base on age:$12 for adults(18 or over),$8 for 
# children.Everyone get  $2 discount on wednesday
age=int(input("Enter your age: "))
day="wednesday"
price =12 if age>=18 else 8
print("The Price of the ticket is ",price)
if day == "wednesday":
    price-=2
    print("The Price of the ticket is ",price)