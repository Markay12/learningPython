# Weight On Certain Planets / Moons
# Demonstrates the use of math and Strings

user_weight = (int)(input("How much do you weigh in pounds?: "))

def moon_weight(weight):
    return weight / 6
    
def sun_weight(weight):
    return weight * 27.1
    
print("\nDid you know that on the moon you would only weigh", moon_weight(user_weight), "pounds?!")
print("\nDid you also know that on the sun you would weight", sun_weight(user_weight), 
"pounds. But, ah... not for too long")

input("\nPress ENTER to exit the program.")
