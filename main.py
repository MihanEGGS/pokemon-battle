print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")
neu = []
import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons")
    print("3. Top 10 weakest pokemons")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        index = int(input("Type an index"))    
        result = pokemons[index]
        print(result)
    elif choice == '2':
        def sortede(pokemons):
            return int(pokemons["attack"])
        neu = sorted(pokemons, key =sortede, reverse = True)
        with open("10_strongest.json", "w") as infile: 
            for i in range(10):
                print(neu[i])
                json.dump(neu[i] , infile)    
    elif choice == '3':
        def sortede(pokemons):
            return int(pokemons["attack"])
        neu = sorted(pokemons, key =sortede, reverse = False) 
        with open("10_wekaest.json", "w") as file: 
            for i in range(10):
                print(neu[i])
                json.dump(neu[i], file)
    elif choice == '4':
        # Battle
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health - lost
        fighter_choice_1 = pokemons[int(input("Choose the fighter of thine"))]
        fighter_random_2 = random.choice(pokemons)
        health_1 = fighter_choice_1["total"]
        health_2 = fighter_random_2["total"]
        while True:
            attack_1 = fighter_choice_1["attack"] - fighter_random_2["defense"] + random.randint(5,20)
            if attack_1 < 0:
                attack_1 = 0 
            health_2 = health_2 - attack_1
            print(fighter_random_2["name"]," ", health_2)
            attack_2 = fighter_random_2["attack"] - fighter_choice_1["defense"] +  random.randint(5,20)
            if attack_2 < 0:
                attack_2 = 0 
            health_1 = health_1 - attack_2
            print(fighter_choice_1["name"]," ", health_1)    
            if health_1 <= 0 or health_2 <= 0:
                if health_1 > health_2:
                    with open("winners.json", "w") as outfile:
                        json.dump(fighter_choice_1, outfile)
                else:
                    with open("winners.json", "w") as outfile:
                        json.dump(fighter_random_2, outfile)        
                break 
    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


