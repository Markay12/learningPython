# Trust Fund Buddy - Bad
# Demonstrates a Logical Error

print(
"""

        Trust Fund Buddy
        
        
    Totals your monthly spending so that your trust fund doesn't run out
    (and you're forced to get a real job).
    
    
    Please enter the requested, monthly costs. Since you're rich, ignore
    pennies and only use dollar amounts.


"""
)

car = (int)(input("BMW Tune Ups: "))
rent = (int)(input("Tempe Apartment: "))
boat = (int)(input("New Boat Rental: "))
gifts = (int)(input("Gifts: "))
food = (int)(input("Dining Out?: "))
staff = (int)(input("Staff (butlers, chef, driver, assistant): "))
games = (int)(input("Computer Games: "))

total = car + rent + boat + gifts + food + staff + games

print("\nGrand Total: ", total)
print("\nFor an average of: ", total // 7, "per item")

input("\n\nPress ENTER to exit the program")


## Selected Type Conversion Functions

# float(x) - returns a floating-point value by converting x, float("10.0") = 10.0
# int(x) - returns an integer value by converting x,  int("10") = 10
# str(x) - returns a String value by converting x,  str(10) = '10'