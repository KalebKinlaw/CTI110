"""
CTI110
P1LAB2 - Sales
kinlawk
8/31
Simple point of sales program 

"""
# set up our store 
store_name = "CTI 110 Hut"
product = "shoes"
stock = 20 
price = 49.99

# Greet Customer
print("Welcome to",store_name)
print("What's your name?")
customer_name = input()
print("Nice to meet you,", customer_name)

# Explain Product
print("Our special today is:", product)
print() #blank line
print("On sale for: $", price)
print("Only", stock, "left!")

#Take order
print("How many", product, "Would you like?")
#input gives us a string
#order = input()
# convert it to a number 
#order = int(order)

# or. . . .
order =int(input())

# Finish up
total_price = order * price
print("So would you like")
print (order,product, "for a total of $", total_price)

print("Thanks for shopping with", store_name)