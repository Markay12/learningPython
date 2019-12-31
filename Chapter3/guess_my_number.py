# Guess My Number
# Demonstrates use of Random Integer and user input if statements

import random

print("""

                            Welcome to 'Guess My Number'!
                            
                            
            I'm thinking of a number between 1 and 100...
            Try to guess it in as few attempts as possible!
                            
                            
      """
      )

attempts = 0
secret_num = random.randint(1, 100)
correct = True


while (correct):

    user_guess = (int)(input("Take a guess!: "))
    
    if (user_guess == secret_num):
        correct = False
        
    elif (user_guess > secret_num):
        attempts += 1
        print("Lower...")
    
    elif (user_guess < secret_num):
        attempts += 1
        print("Higher...")
    
if (user_guess == secret_num):
    attempts += 1
    print("\nYou guessed it! The number was", secret_num)
    
    if(attempts > 1):
        print("And it only took you", attempts, "tries!")
    else:
        print("And it only took you", attempts, "try!")
        
    
    
    
input("\n\nPress ENTER to exit the program.")
