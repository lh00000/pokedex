import csv
import random
import webbrowser
import time


pokemon = []
with open('Pokemon.csv', 'r') as file: #using with method to open file, file automatically closes
  reader_variable = csv.reader(file, delimiter = ",")
  #Seperates the data into header and data
  header = next(reader_variable)
  # Pokemon can be used as a list without needing to open it up
  for row in reader_variable:
    pokemon.append(row)
  
print("""
                                                                                
                                                                                
                                                                                
                            /@@@@@@@@@@@@@@@@@@@@@@@.                           
                       &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                      
                   (@@@@@@@@@@@###################@@@@@@@@@@@.                  
                *@@@@@@@@@#############################@@@@@@@@@                
              @@@@@@@@#####################################@@@@@@@/             
            &@@@@@@%#########################################%@@@@@@*           
          .@@@@@@##############################################%@@@@@@          
         &@@@@@@#################################################@@@@@@,        
        &@@@@@#####################################################@@@@@*       
       %@@@@@######################@@@@@@@@@@@######################@@@@@       
       @@@@@%###################@@@@@@@@@@@@@@@@@###################%@@@@@      
      &@@@@@##################@@@@@%         @@@@@%##################@@@@@.     
      @@@@@@%%%%%%%%%%%%%%%%%@@@@@            *@@@@%%%%%%%%%%%%%%%%%%&@@@@&     
      @@@@@@@@@@@@@@@@@@@@@@@@@@@&             @@@@@@@@@@@@@@@@@@@@@@@@@@@&     
      @@@@@                  #@@@@.           (@@@@.          ...... @@@@@%     
      &@@@@#                  %@@@@@        /@@@@@,           ......,@@@@@      
       @@@@@                    @@@@@@@@@@@@@@@@#            .......@@@@@&      
       (@@@@@                      (@@@@@@@@@.               ......&@@@@@       
        #@@@@@                                              ......@@@@@@.       
         /@@@@@/                                           ..... @@@@@@         
           @@@@@@                                        ......@@@@@@@          
            (@@@@@@*                                    .....@@@@@@@            
              /@@@@@@@                                ....@@@@@@@@              
                 @@@@@@@@@                         ...%@@@@@@@@&                
                    @@@@@@@@@@@%                (@@@@@@@@@@@%                   
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                       
                             *@@@@@@@@@@@@@@@@@@@@@.                            
                                                                                
                                                                                """)
flag = True
rotomusage = 0
infousage = 0
pokedexusage = 0
fun = 0
pokecoin = 0
shopopen = 0
inventory = []

while flag:
  print('''Welcome to the POKEMON SUPER SEARCH ENGINE!\n
  1. Display Pokemon
  2. Display First Pokemon of type
  3. Display Pokemon by total base stats
  4. Display Pokemon by minimum stats
  5. Display Legendary Pokemon
  6. Rotom Flip
  7. More info
  0. Quit\n '''
  )
  options = input("Enter option: ")
  print()

  def print_header():
      """Prints the header for the pokedex"""
      print("{:<2} {:<25} {:<8} {:<8} {:<6} {:<3} {:<7} {:<8} {:<8} {:<8} {:<6} {:<11} {:<10}".format(*header))

  def print_pokemon(i):
      """Prints the pokemon data"""
      print("{:<2} {:<25} {:<8} {:<8} {:<6} {:<3} {:<7} {:<8} {:<8} {:<8} {:<6} {:<11} {:<10}".format(*pokemon[i]))

  
  if options == "1":
    pokedexusage += 1
    try:
      n = int(input("Enter number of Pokemon to be displayed: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
    i = 0
    while n < 1 or n > 800: #validating input
      print("Please enter a number between 1 and 800 (inclusive)\n") #printing error message
      n = int(input("Enter number of Pokemon to be displayed: "))
    if n > 0 and n < 801:
       print_header()
       while i < n: 
            print_pokemon(i) #calls function print_pokemon() to format output 
            i += 1
    print()

  if options == "2":
    pokedexusage+=1
    types = [row[2] for row in pokemon] #creates a list by appending the item with index = 2 for each row
    types.append([row[3] for row in pokemon]) #append items with index = 3 for each row so as to ensure that all valid types are in list
    type = (input("Enter type: ")).title() #makes programme non-case sensitive
    found = False
    i = 0
    if type not in types: #checking if it is a valid type
        print("No pokemon of this type.\n")
        found = True

    while found is False and i <= 799: 
        if type == pokemon[i][2] or type == pokemon[i][3]: 
            print_header()
            print_pokemon(i)
            found = True
            print()
        else: 
            i += 1

  if options == "3":
    pokedexusage += 1
    stat = input("Enter Total Base stat: ")
    i = 0
    stats = [row[4] for row in pokemon] #creates a list by appending the item with index = 4 for each row
    if stat in stats: # checking that input is valid (if there are pokemon with requested total base stat)
        print_header()
        while i <= 799: #such that program will check through all pokemon for ones that meet provided conditions
            if stat == pokemon[i][4]:
                print_pokemon(i)
            i += 1
        print()
    else:
        print("No pokemon with this Total Base stat.\n")  

  if options == "4":
    pokedexusage += 1
    special_attack = int(input("Enter min special attack stat: "))
    special_defense = int(input("Enter min special defense stat: "))
    speed = int(input("Enter min speed stat: "))
    yes = 1
    for row in pokemon:
      if special_attack <= int(row[8]) and special_defense <= int(row[9]) and speed <= int(row[10]): #checking if the inputted special stats are valid (if there are pokemon with requested special stats))
        yes += 1 
    
    if yes == 1:
      print("No pokemon has such powerful stats.\n")
    else:
      print_header()
      for row in pokemon:
        if special_attack <= int(row[8]) and special_defense <= int(row[9]) and speed <= int(row[10]):
          print_pokemon(pokemon.index(row))

  if options == "5":
    pokedexusage += 1
    type1 = (input("Enter Type 1: ")).title() # title to ensure programme is not case sensitive 
    type2 = (input("Enter Type 2: ")).title()
    yes = 0
    for row in pokemon:
      if type1 == row[2] and type2 == row[3] and row[12] == "TRUE": #checking if the inputted types are valid (if there are legendary pokemon with requested types)) 
        yes += 1
    if yes == 0:
      print("No such legendary pokemon.")
    else:
      print_header()
      for row in pokemon:
        if type1 == row[2] and type2 == row[3] and row[12] == "TRUE": 
          print_pokemon(pokemon.index(row))

  if options == "0":
    print("Thank you for using the POKEMON SUPER SEARCH ENGINE!")
    flag = False # exits the program

  if options == "6":
    rotom_flag = True
    print("Rotom Flip is booting...")
    # Makes it lag as if there wa actual processing time
    time.sleep(2)
    print()
    print("Rotom Flip is ready!")
    print("""
By using Rotom Flip, you agree to the following:

Rotom Flip can collect your personal information and use it to improve the service.
Rotom Flip will not be responsible for any damages caused by using this service.
Rotom Flip will not be held responsible for any illegal activities.
Rotom Flip will hold you accountable for any statements made using Rotom Flip.
Rotom Flip can send you marketing emails with the provided email.
""")
    emailflag = True 
    email_data = []
    while emailflag:
      email = input("Please input your email: ")
      # Checks if email address is valid
      if email.count("@") == 0 or email.count(".") == 0:
        print("Invalid email.")
      elif email.count("edu")!=0:
        print("Your administrator has blocked this application.")
      elif email == "quit":
        print("Make an email and try again.")
      else:
        rotomusage += 1
        email_data.append(email)
        emailflag = False
    print()
    while rotom_flag:
      print("Welcome to Rotom Flip!")
      print()
      print("Local time:" , time.ctime(time.time()+28800))

      apps = input("""
  1. Pokegames
  2. Chat with Pokemon
  3. DO NOT USE
  4. PokeShop
  5. Inventory
  0. Back
  
  Enter number of application: """)
      print()
      if apps == "1":
        print("Welcome to the Pokegames!")
        game = input("""
        Game options:
          
        1. Pokemon Arena
        2. Guess the Pokemon!
          
        Which game would you like to play? """)
        print()
        if game == "1":
            flag_game = True
      
            while flag_game:

              print("Welcome to the Pokemon Arena. Choose your pokemon.")
              print("""
              1. Charmander
              2. Bulbasaur
              3. Squirtle
      
              0. Quit
      
              """)
              # Ask for input from user
              pokemon_choice = input("Enter the number of the pokemon you want to choose: ")
              # Pokemon stats
              if pokemon_choice == "1":
                print("You chose Charmander!")
                hp = 100
                atk = 30
                defense = 10
      
              elif pokemon_choice == "2":
                print("You chose Bulbasaur!")
                hp = 100
                atk = 20
                defense = 20
      
              elif pokemon_choice == "3":
                print("You chose Squirtle!")
                hp = 100
                atk = 20
                defense = 30
              # Exits the game
              elif pokemon_choice == "0":
                print("Thank you for playing.")
                flag_game = False
                hp = 0
                
              # Because you failed to follow the instructions
              else:
                print("You chose Paper!")
                hp = 1
                atk = 1
                defense = 1
      
              Comp_HP = 100
              # For healing
              i = 0
              while hp > 0 and Comp_HP > 0:
                print("Your pokemon has", hp, "HP")
                print("The computer's pokemon has", Comp_HP, "HP")
                print()
                action = input("What would you like to do? (Smack/Heal(use only once)): ").capitalize()
                # Attacks
                if action == "Smack":
                  oppdmg_taken = atk - 5
                  print("The opponent has taken",oppdmg_taken,"damage!")
                  Comp_HP -= oppdmg_taken
                  print()
                  print("The opponent's turn begins...")
                  print()
                  print("The opponent used Smack!")
                  # Damage dealt scales on defense of pokemon
                  if defense == 10:
                    dmg_taken = 20 - 5
                  elif defense == 20:
                    dmg_taken = 20 - 10
                  elif defense == 30:
                    dmg_taken = 20 - 15
                  else:
                    dmg_taken = 20
                  print("Your pokemon has taken", dmg_taken, "damage!")
                  print()
                  hp -= dmg_taken
                if action == "Heal":
                  i += 1
                  # Prevents heal from being used more than once
                  if i > 1:
                    print("You cannot use Heal again! You have used all of your Heals!")
                    print()
                  else:
                    if hp<80:
                      hp += 20
                    else:
                      hp = 100
                    print("Your pokemon has healed! Your HP is now", hp)
                    print()
                    print("The opponent's turn begins...")
                    print()
                    # Let opponent 
                    print("The opponent used Smack!")
                    # Damage dealt scales on defense of pokemon
                    if defense == 10:
                      dmg_taken = 20 - 5
                    elif defense == 20:
                      dmg_taken = 20 - 10
                    elif defense == 30:
                      dmg_taken = 20 - 15
                    else:
                      dmg_taken = 21
                    print("Your pokemon has taken", dmg_taken, "damage!")
                    print()
                    hp -= dmg_taken
                
                # The almost only way for you to lose
                
                if Comp_HP <= 25:
                  print("The opponent's pokemon suddenly became super powerful! Watch Out!")
                  print("...")
                  last_words = input("Do you have any last words? (Yes/No): ").capitalize()
                  if last_words == "Yes":
                    last = input("What are your last words?: ")
                    print()
                    # Condition to win
                    if last.find("full marks") != -1 or last.find("Full marks") != -1:
                      print("The opponent's pokemon has suddenly fainted! You win!")
                      print("Pokecoin + 10")
                      pokecoin += 10
                      Comp_HP = 0
      
                    else:
                      print("Goodbye. A clue for you: Since this pokedex is so good...")
                      print()
                      print("The opponent used SMACK!!")
                      print("Your pokemon has fainted. GAME OVER")
                      print("Pokecoins -10")
                      pokecoin -= 10
                  else:
                    print("The opponent used SMACK!!")
                    print("Your pokemon has fainted. GAME OVER")
                    print("Pokecoins -10")
                    pokecoin -= 10
                  playagain = input("Play again? (Y/N):").capitalize()
                  # Allows you to play again
                  if playagain == "Y":
                    Comp_HP = 0
                  else:
                    Comp_HP = 0
                    flag_game = False
              if hp == 0:
                print("Your pokemon has fainted. GAME OVER")
        if game == "2":
          # Guess the pokemon
          score = 0
          print("Welcome to Guess the Pokemon! Prepare your pokemon hat and let's get started!")
          print()
          # Two sets of pokemon questions
          question = random.randint(1,2)
      
          if question == 1:
            print("Guess the pokemon!")
            print()
            print("""  . .. .  .    .  .    .  .    .  .  . .  . .. .  .    .  .    .  .    .  .  . .
                                                               *@                     
       . .  .    .  .    .  .    .  .    .  .  . .  .    . .@@@@%.  .    .  .    .  . 
      .. .  .  . .  .    .  .    .  .  . .  . .. .  .  . @@@@@@@ .  .    .  .  . .  . 
      .. .  .    .  .    .  .    .  .    .  . .. .  . (@@@@@@@#  .  .    .  .  . .  . 
      .. .  .    .  .    .  .    .  .    .  . .. .  /@@@@@@@@    .  .    .  .  . .  . 
      .. .  .   *(%%%%(/*,  .    .  .    .  . .. . @@@@@@@@ .    .  .    .  .  . .  . 
      .. .  .    #@@@@@@@@@@@@@@@@# &@@@@@@@@@@@@@@@@@@@@.  .  @ .  .    .  .    .  . 
                      (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&     #@@@@@@&                  
                               @@@@@@@@@@@@@@@@@@@@@@@/   @@@@@@@@@@@@@&              
                              @@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@           
        . .  .  .    .  .    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    .  .  . .
        . .. .  .    .  .   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.  .  . .  .  . .
        . .. .  .    .  .   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .  .  . .  .  . .
        . .. .  .    .  .    .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%  .  . .  .  . .
        . .. .  .    .  .    .  ,@@@@@@@@@@@@@@@@@@@@@@ .   #@@@@@@@@@@@@, . .  .  . .
        . .. .  .    .  .    .   @@@@@@@@@@@@@@@@@@@@@@@.  ,@@@@@@@@@.  .    .  .  . .
                                ,@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@.                   
                                %@@@@@@@@@@@@@@@@@@@@@@@@@    %@@@@@@@*               
                               ,@@@@@@@@@@@@@@@@@@@@@@@@@@%  (@@@@@@,                 
       . .  .    .  .    .  .  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.  .    .  .    .    
      .. .  .    .  .    .  .  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@(    .  .    .  .  . .  . 
      .. .  .    .  .    .  .  @@@@@@@@@@@@@@@@@@@@@@@@@@@@ .    .  .    .  .  . .  . 
      .. .  .    .  .    .  .   %@@@@@@@@@@@@@@@@@@@@@@@@&  .    .  .    .  .    .  . 
      .. .  .    .  .    .  .   #@@@@@@%.      ,/#@@@@@@@   .    .  .    .  .    .  . 
      .. .  .  . .  .    .  . ,@@@@@,  . .  . .. .  *@@@@&  .    .  .  . .  .  . .  . 
                                                      .@@%                            
                .    .  .    .       .                       .  .    .       .        """)
            answer_1 = input("What is this pokemon? ").title()
            # Checks if answer is correct and award points accordingly
            if answer_1 == "Pikachu":
              print("Correct! Next question.")
              score += 1
            else:
              print("Incorrect. Go play more pokemon.")
            print()
            time.sleep(1)
            print("""                                                                        
                                                                .@@   @@            
                                                              @@@@@@@@@,            
                                          ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                                     .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           
                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           
                 @@@@@@@%         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
               *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
              *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%       
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
         #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(      
           #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%       
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                   @@@@@@@@@@@@@@&    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
                    @@@@@@@@@@@@        @@@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@         
                    @@@@@@@@@@            @@@@@@@@@@@@@       @@@@@@@@@@@(          
                                            %@@@@@@                                 
                                                                                   """)
            
            answer_1 = input("What is this pokemon? ").title()
            if answer_1 == "Bulbasaur":
              print("Correct! Next question.")
              score += 1
            else:
              print("Incorrect. Go play more Pokemon.")
            print()
            time.sleep(1)
            print("""                                                                                
                                  &(@@@&                                            
                             ./   @@@@@@@@@@@@/                                     
                       .*%@@@&     @@@@@@@@@@@@@@@*            .@#                  
                  .@@@@@@@@@@        @@@@@@@@@@#   (             @@/                
               #@@@@@@@@@@@@@%            @@@@@@                *@@@@@@*            
            &@@@@@@@@@@@@@@@@@%           .@@@@@@              @@@@@@@@@@           
           @@@@@@@@@@@@@@@@@@@@,           @@@@@@,           ,@@@@@@@@@@@@@(        
          @@@@@@@@@@@@@@@@@@@@@@@@@/       @@@@@@@          &@@@@@@@@@@@@@@@@@#     
        %@@@@@#      %@@@@@@@@@@@@@@@@@#,. @@@@@@@/   .#@@@@@@@@@@@@@@@@@@@@@@@.    
        @@@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
        @@(             /@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*   #@@@@@@@,   
        /@                   *@@@    &@@@@@@@@@@@@@@@@#   *@@@@@@@@    #@@@ .@@@(   
         *               .@@@@@@@*   @@@@@@@@@@@@@@@@@     *@@@@@&     .@@@#  @@(   
                            @& (@, @@@@@@@@@@@@@@@@@@@@   .@/ @@ (    #@@@@,  (@,   
                                 %@@@@@@@@@@@@@@@@@@@@@%              &@@@@@@ *.    
                      .%@@@&%*.@@@@@@@@@@@@@@@@@@@@@@@@@@             #@@@@@@       
                   &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%           ,@@*         
                 &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       *@@            
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.                 
                   ,@@@@@@@@@@@@@@..                 ..(@@@@@@@                     
                         ,@@@@@@@                         .&@%@&/                   
                            &   /                                                 
    """)
    
            answer_1 = input("What is this pokemon? ").title()
            if answer_1 == "Charizard":
              print("Correct! This is the end.")
              score += 1
            else:
              print("Incorrect. Go play more Pokemon.")
            print()
            print("Your score is " + str(score) + "/3.\n")
            if score == 3:
              print("Pokecoins +5")
              pokecoin += 5
            else:
              print("Pokecoins -1")
              pokecoin -= 1
            # Advertisement for you because you lost
            if score == 0:
              print("This is an ad. You have to watch it.")
              print()
              time.sleep(1)
              print("Taken from Pokemon LIVE...")
              print("In the darkness we hear the opening strains of the POKÉMON THEME. It will serve as an overture. With the final note, everything goes black. The television screens flash on. MYSTERY MAN's commercial plays. The opening image is some fabulous montage of Pokémon with Voice Over. MYSTERY MAN is actually GIOVANNI.")
              time.sleep(5)
              print("""
MYSTERY MAN(GIOVANNI): (Voice Over) Attention all Pokémon Trainers! Announcing the all new...Diamond Badge.

There's a magical video effect. And we see asexy product shot of the Badge)

Diamonds are the hardest substance on Earth. And the Diamond Badge is the hardest Pokémon Badge on Earth to win. There's only one to be won!

(The phrase, "Only One To Be Won" flashes across the screens)

Only one way to win it..
""")
              time.sleep(7) 

              print("""The phrase, "Only One Way To Win It" flashes across the screens) Only one way to make it yours, and yours alone.(There is some magical video effect. Suddenly, MYSTERY MAN appears on screen, holding the badge)

MYSTERY MAN (GIOVANNI) (On Screen): By defeating me and my Pokémon in a Pokémon battle. Are you Trainer enough to try? If so, check out our website at www.diamondbadge.com...

(The address flashes across the screen, as a fabulous shot of the map also fills the screen)

...and download a copy of the map to where the battles are to take place.

(The visual is once again MYSTERY MAN, now holding the badge)

The Diamond Badge is waiting...for...you!

(There is another magical video effect and the screen goes black. Set changes to ASH's bedroom. ASH is in bed. PIKACHU is hiding under the covers...unseen for the moment. As the set is moving into place, MRS. KETCHUM and PROFESSOR OAK are crossing into it. THEY are each dressed to go out)
""")
              time.sleep(10)
    
          if question == 2:
            print("Guess the pokemon!")
            print()
            print("""                                                                                
                @@@#(@@@                                                            
             ./ .&@& @@.*@@@                                                        
            /@@@@/@@@@@@@@                                                          
                &@@@@@@@@&@@@@#                        .@@@@@@#                     
                 @@@@@@@@@@@@@@@@#*##/. .*/*.       .@@@@@@@@@@@@&                  
                 .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/               
                ( @@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,      /@@#             
                 #@@,      @@@@@@@@@@@@@@@@@@@@@@@@@@@&                             
                 @@@        /#(,@@@@@@@@@@@@@@@@@@@@@(*                             
                ,@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                     .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#&@@@                 
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@&                
                         #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,       @@@                
                            .@@@@@@@@@@@@@@@@@@@@@@@@@%         #@@@@@*             
                             *@@@@@@@@@@@@@@@@@@@@@@@@      #%&@@@@@@@@@@@@@        
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@    %@@  .@@@@@(@@@@         
                           &@@@@@@@@@@@@@@@@@@@@@@@@@@@%        @@@ /@@( ,,         
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.      /(   ..             
                      %@@@@#   .,.  .@@@@@@@@@/  /%%*  /@@@@@@                      
                   ,@@@@@@@@#                            .@@@@                      
                      .  (@@@@%                           @@@@&                     
                    /@@@   @@@@@@,                          @@@@*                   
                   %@@. &@@@@@@@#                          @@@@@@@@@@.&@*           
                    @@@@@@@@@/                              #@@@@@@@@@@@@           
                       .,                                       @@@@@@@             
                                                                                   """)
            answer_2 = input("What is this pokemon? ").capitalize()
            if answer_2 == "Mr. mime" or answer_2 == "Mr. Mime" or answer_2 == "Mr mime":
              print("Correct! Next question.")
              score += 1
            # If you know your pokemon memes
            elif answer_2 == "Ash's dad":
              print("Unable to judge. No scores awarded.")
              webbrowser.open("https://www.youtube.com/watch?v=Lz66lfSlGtc")
            else:
              print("Incorrect. Go play more Pokemon.")
            print()
            time.sleep(1)
            print("""                                                                                
                                                                                    
                      &@@                                                           
                      &@@@@(                                                        
                      %@@@@@@@.                                                     
                      /@@@@@@@@@@                                                   
                      .@@@@@@@@@@@@* &@@  @.   .#@@@@@@*                            
                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                              
         .**@@@@/      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
          *@@@@@@@@@%  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,    
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(       
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%          
              %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&             
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                   
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
               /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%        
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(      
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#              
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.                   
             .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                        
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                           
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                            
               .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(                            
                  %@@@@@& &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                            
                     .@       .@@@@@@@@@@@@@@@@@@@@@@@@(                            
                                 @@@@/   (@@@@@@@@@@@@(                             
                                           @@@@@@@@@@                               
                                            @@@@@@                """)
            answer_2 = input("What is this pokemon? ").title()
            if answer_2 == "Gengar":
              print("Correct answer. Next question.")
              score += 1
            else:
              print("Incorrect. Go play more Pokemon.")
            print()
            time.sleep(1)
            print("""                                                                                
                                  .%@@@@@@@@@@@@@@@@@%,                             
                            /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                       
                        &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%             
                &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           
              #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/         
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
         &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(    
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
        *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.   
        &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,   
        *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,    
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
           *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%        
              #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,           
                  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.             
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                
                        &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                   
                            ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                       
                                   *@@@@@@@@@@@@@@@@@/                         """)
            answer_2 = input("What is this pokemon? ").title()
            if answer_2 == "Electrode":
              print("Correct! This is the end.")
              score += 1
            else:
              print("Incorrect. Go play more Pokemon.")
            print()
            # Prints your score
            print("Your score is " + str(score) + "/3.\n")
            if score == 3:
              print("Pokecoins +5")
              pokecoin += 5
            else:
              print("Pokecoins -1")
            if score == 0:
              print("This is an ad. You have to watch it.")
              print()
              time.sleep(1)
              print("POKEMON UNITE")
              print("""Pokémon UNITE is a strategic team battle game developed jointly by The Pokémon Company and Tencent Games’ TiMi Studios. Pokémon UNITE is a free-to-start, cross-platform game available on Nintendo Switch and mobile devices.

In this game, players face off against each other in 5-on-5 team battles. During battles, you will cooperate with teammates to defeat wild Pokémon, level up and evolve your own Pokémon, and knock out opponents’ Pokémon while trying to earn more points than the opposing team within the allotted time. Pokémon UNITE introduces a new kind of Pokémon battle—one that requires teamwork and strategy. It is simple and yet full of intricacies waiting to be unpacked.


""")
              time.sleep(6)
              print("""POKEMON SLEEP
Do you find yourself struggling to get energized in the morning? Has the same old bedtime routine grown tiresome? Now, you can turn your sleep into entertainment with Pokémon Sleep! Playing this game is simple: just place your smartphone by your pillow, then go to sleep. Just like that, waking up in the morning becomes something to look forward to!

Your adventure takes place on a small island where you’ll carry out research on how Pokémon sleep. You’ll work with large Snorlax who live on the island and Neroli, a professor who’s studying Pokémon sleep styles.


            """)
              time.sleep(6) 

              print("""POKEMON SMILE
Motivating children to brush their teeth can be tough, but with Pokémon Smile, brushing becomes an exciting adventure! This free-to-play game uses your smart device’s camera, allowing children to brush their teeth to rescue Pokémon that have been captured by cavity-causing bacteria.

Skillful brushing will defeat the troublesome bacteria and make the captive Pokémon appear. If kids brush their teeth well, they will be able to rescue the Pokémon. There are over 100 species of Pokémon to rescue, so kids will want to keep coming back to brush in order to complete their Pokédex.

By brushing regularly, children can also earn amusing Pokémon Caps that will appear on their head in the game as they brush. Kids will love seeing themselves wearing a Pokémon hat or even looking like a Pokémon! They can decorate pictures of themselves wearing the Pokémon Caps to create all sorts of silly images.
            """)
              time.sleep(10)
  
      if apps == "2":
        # Opens webpage to Pikachu Chatbot
        webbrowser.open("https://c.ai/c/zKKxMakC7QasF1gpW0NSH6Z29P9n_qKwehOgsgHh-os")

      if apps == "3" and fun == 0:
        fun += 1
        print("I see that you did not heed the name.")
        print("Okay then.")
        # Opens video
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        time.sleep(6)
        # Create a countup to 667 seconds but will print 666
        def repeat():
          try:
            for i in range(667):
              print(i)
              time.sleep(1)
          # Prevents Keyboard Interrupr
          except KeyboardInterrupt:
            repeat()
        repeat()
      elif apps == "3" and fun > 0:
        fun += 1
        # Makes it 1000 seconds now
        def repeat():
            try:
                for i in range(1000):
                  print(i)
                  time.sleep(1)
            except KeyboardInterrupt:
                repeat()
        repeat()
      
      if apps == "4":
        if fun >= 10: #checking if user has had enough fun 
          shopopen = 1
        elif shopopen == 0: 
          print("Please reach 10 fun points to unlock this application. Else, you can consider paying our pay now under more info to unlock the shop.")
          
        if shopopen == 1:
          print('Welcome to the Pokeshop!')
          yipee = True
          while yipee:
            print("Pokecoins: " + str(pokecoin))
            try:
              choice = int(input('''What would you like to buy?
  1. Waffle (10 pokecoins)
  2. Iced coffee (20 pokecoins)
  3. Iced tea (20 pokecoins)
  4. Hot dog (50 pokecoins)
  5. Surprise me! (10000 pokecoins)
  6. Pokecoins (SGD $5)
            '''))
            except ValueError:
              print("Please input a number.")
            else:
              yipee = False 
              if choice == 1: 
                if pokecoin >= 10:
                  pokecoin -= 10 
                  print("Congratulations! You have bought a waffle! You have", pokecoin, "pokecoins left.")
                  inventory.append("Waffle")
                else:
                  print("Insufficient pokecoins!")
              elif choice ==2:
                if pokecoin >= 20:
                  pokecoin -= 20
                  print("Congratulations! You have bought an iced coffee! You have", pokecoin,"pokecoin left.")
                  inventory.append("Iced coffee")
                else: 
                  print("Insufficient pokecoins!")
              elif choice == 3:
                if pokecoin >= 20:
                  pokecoin -= 20
                  print("Congratulations! You have bought an iced tea! You have", pokecoin,"pokecoins left.")
                  inventory.append("Iced tea")
                else:
                  print("Insufficient pokecoins!")
              elif choice == 4: 
                if pokecoin >= 50:
                  pokecoin -= 50
                  print("Congratulations! You have bought a hot dog! You have", pokecoin,"pokecoins left.")
                  inventory.append("Hot dog")
                else: 
                  print("Insufficient pokecoins!")
              elif choice == 5:
                if pokecoin >= 10000:
                  pokecoin -= 10000
                  print("Congratulations! You have bought a surprise me! You have", pokecoin,"pokecoins left.")
                  inventory.append("Surprise me!")
                else:
                  print("Insufficient pokecoins!")
              elif choice == 6:
                print("Please head to More Info to pay.")
              print()

      if apps == "5":
        print("Opening Inventory...")
        print("Your inventory contains:")
        print("Pokecoins: " + str(pokecoin))
        print()

        # Prints out items in inventory
        if inventory.count("Waffle") > 0:
          print("Waffle:", inventory.count("Waffle"))
        if inventory.count("Iced coffee") > 0:
          print("Iced coffee:", inventory.count("Iced coffee"))
        if inventory.count("Iced Tea") > 0:
          print("Iced tea:", inventory.count("Iced tea"))
        if inventory.count("Hot dog") > 0:
          print("Hot dog:", inventory.count("Hot dog"))
        if inventory.count("Surprise me!") > 0:
          print("Surprise me!:", inventory.count("Surprise me!"))

        # Input to get more info about items in inventory
        i_info = input("What item would you like to know more about? ").capitalize()

        # Prints out info about items in inventory
        if i_info == "Pokecoins":
          print("A shiny coin that can be used to buy items in the shop.")
        elif i_info == "Waffle" and inventory.count("Waffle") > 0:
          print("Crispy on the outside, soft and fluffy jigglypuff dancing on the inside.")
        elif i_info == "Iced coffee" and inventory.count("Iced coffee") > 0:
          print("Better than hot coffee, it's cool and refreshing. Eevee sleeps inside it.")
        elif i_info == "Iced tea" and inventory.count("Iced tea") > 0:
          print("Tea that has been cooled. Charmander attempts to turn it into hot tea.")
        elif i_info == "Hot dog" and inventory.count("Hot dog") > 0:
          print("A sausage stuffed in a bun, with wayyy too much ketchup on it.")
        elif i_info == "Surprise me!" and inventory.count("Surprise me!") > 0:
          # Runs animation
          import os
          for i in range(0,37):
            f = open("pikachutxt/frame"+str(i)+".txt","r")
            file_contents = f.read()
            # Clears the screen
            os.system('cls' if os.name == 'nt' else 'clear')
            # Prints the frame
            print(file_contents, end = "\r")
            time.sleep(0.3)
        else:
          print("There is no such item.")
        print()
        

      if apps == "0":
        print("Thank you for using Rotom Flip.")
        print()
        # Exits Rotom Flip app
        rotom_flag = False
      
  if options == "7":
    print("Welcome to the more info page!")
    print("""
You must want to know more about the team behind this project and how it was made?
Well, you've come to the right place!
    """)
    flag_info = True
    # Data collection
    infousage += 1
    while flag_info:
      print("""
Menu:  
  1. Team
  2. How it was made
  3. About the program
  4. Redeem codes
  0. Back
      """)
      
      info = input("Enter the number of the information you want to know: ")
      print()
      
      if info == "1":
        print("""
The team behind this project is:
  1. Jessie Tangsy
  2. Naomi Tan Tan
  3. Le Han Yauuuu
        """)
        
      if info == "2":
        print("""
This program was made using python, blood, sweat and tears. And your kindness...
        """)

        # Printing data of how many times you have used the certain programs
        if pokedexusage > 10:
          print("You have used the actual pokedex features " + str(pokedexusage) + " times. You really wanted to find a bug huh.")
          
        if rotomusage>1:
          print("Thank you for showing much love for our Rotom Flip by visiting it",rotomusage, "times!")
          
        if infousage>1:
          print("You either really want to fund us, have a thing for seeing your own data or you want to stalk us. You have visited this page",infousage,"times.")
        print("Fun:", fun)
        print("There will be a surprise when your fun level reaches 10!")
        
      if info == "3":
        print("""
This program is a Pokemon Super Search Engine.
  
If you wish for it to be better and more enjoyable, do consider funding us! We are just a few poor students with poor equipment and need YOUR support!

To fund us, please Pay Now us at: XXXX XXXX
(You know how to find us)
There may be a hidden surprise for you!
  
Thank you and have a great day!
        """)

      if info == "4":
        code = input("Enter redeem code: ")
        
        if code == "paywall064920-@#$":
          # Sponsor benefits
          betterbenum = True
          print("Thank you for your support! We will now be able to make this program better!")
          print("You want a special surprise right? Well, you've come to the right place!")
          # Complete the Square program
          print("""
  Booting up the program...
  
  Welcome to Complete the Square!
  
  ax² + bx + c = 0
  """)
          while betterbenum:
            try:
              a = float(input("Enter a (must be num): "))
            except ValueError:
              print("Invalid input. Please enter a number.")
            else:
              try:
                b = float(input("Enter b (must be num): "))
              except ValueError:
                print("Invalid input. Please enter a number.")
              else:
                try:
                  c = float(input("Enter c (must be num): "))
                except ValueError:
                  print("Invalid input. Please enter a number.")
                else:
                  betterbenum = False
                  print()
                  h = b/(2*a)
                  k = c - b**2/(4*a)
                  print(a, "(x +", h, ")² +", k)
                  time.sleep(3)
                  webbrowser.open("https://www.youtube.com/watch?v=vikINVCvqCE")
  
        if code =="3xtrap4ywallpok3c0ins":
          # Pay to win
          pokecoin += 10000
          print("Pokecoins have been added to your account.")

        if code == "morepaywall2024#@$%":
          shopopen = 1
          print("Shop has been unlocked!")
      
      if info == "0":
        # Exits more info page
        flag_info = False
        

  
  if fun == 10:
    print("It's been 10 funfilled rides.")
    print("But I'm sure you have had a lot of fun since you did it 10 times. So I'll let you have it.")
    print("SURPRISE!!")
    print("You gained 10000 pokecoins!")
    pokecoin += 10000
    print("Shop has been unlocked!")
    # Opens shop
    shopopen = 1
    
    

   
  
    
