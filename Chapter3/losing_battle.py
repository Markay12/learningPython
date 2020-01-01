# Losing Battle
# Demonstrates the dreaded infinite loop

print(
      """
      
                        Your lone hero is surrounded by a massive army of trolls!
                    Their decaying green bodies stretch out, melting into the horizon
                    
                      Your hero unheathes his sword for the last fight of his life.
                      
     """  
     )
     
health = 9
trolls = 0
damage = 3

while health != 0:
    trolls += 1
    health -= damage
    
    print("Your hero swings and defeats an evil troll, " \
          "but take", damage, "damage points.\n")
          
          
input("\n\nPress the ENTER key to exit the program.")