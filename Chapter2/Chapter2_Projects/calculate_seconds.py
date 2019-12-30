# Calculate Seconds
# Demonstrates how to use math to convert years to seconds

conversion_factor = 365 * 24 * 60 * 60

def convert(years):
    years *= conversion_factor
    return years
    
age = (int)(input("How old are you?: "))

print("\nDang! That means you've lived", convert(age), "seconds")

input("\nPress ENTER to exit the program.")