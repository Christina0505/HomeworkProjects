# Ask user for two numbers
number1 = input("Give me a number ")
number2 = input("Give me another number ")
# Create a loop that does the following until the product and sum are the same
sum = int(number1) + int(number2)
product = int(number1) * int(number2)
while (sum != product):
# Calculate and display their sum
    print ("The sum is..."+str(sum))
# Calculate and display their product
    print ("The product is..." + str(product))
# If their sum and their product are equal - tell the user
# otherwise ask for two more numbers
    print ("The sum does not equal the product")
    number1 = input("Please give me a different number ")
    number2 = input("Give me another number ")
    sum = int(number1) + int(number2)
    product = int(number1) * int(number2)
print ("The sum and product are equal")
