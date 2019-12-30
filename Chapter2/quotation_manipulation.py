# Quotation Manipulation
# Demonstrates String Methods

# quote from IBM Chairman, Thomas Watson, in 1943
quote = "I think there is a world market for maybe five computers"

print("Original Quote: ")
print(quote)

print("\nQuote in UpperCase: ")
print(quote.upper()) # Manipulates quote to upper case

print("\nQuote in LowerCase: ")
print(quote.lower()) # Manipulates quote to lower case

print("\nQuote as a Title: ")
print(quote.title()) # Manipulates quote to a title

print("\nQuote with a minor replacement: ")
print(quote.replace("five", "millions of")) # manipulates the quote to replace the first word with your second parameter

print("\nOriginal Quote is still: ")
print(quote) # still prints the same quote 

input("\n\nPress the ENTER key to exit the program.")


# Title capitalizes the first letter of every word


## Useful String Methods
# ---------------------------------
# upper() - Returns the uppercase version of the String
# lower() - Returns the lowercase version of the String
# swapcase() - Returns a new string where the case of each letter is switched. (Uppercase becomes lower and lower becomes upper)

# capitalize() - First letter is capitalized and the rest is lowercase

# title() - Returns a new string where the first letter of each word is capitalized

# strip() - returns a string where all of the white space and spaces are removed from the beg, middle and end of the String

# replace(old, new[,max]) - returns a string where occurances of the String old are replaced with the new.
# The optional max limits the number of replacements 
