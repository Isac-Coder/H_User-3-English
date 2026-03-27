import os
WHITE = '\033[1;37m'

if os.path.exists("database.txt"):
    pass
else:
    with open ("database.txt", "w") as file:
        pass

with open("database.txt", "r") as file:
    contador = len(file.readlines())


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{WHITE}MENU\n")
    print("Choose 1 for the Daily Blocker")
    print("Choose 2 to display the daily blockers")
    print("Choose 3 to clean the database")
    print("Choose 4 to exit the program or exit for close the program\n")

    option = input("Enter an option:\n# ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if option == "1":
        blocker = input("\nEnter your Daily Blocker:\n# ")
        contador += 1
        with open ("database.txt", "a") as file:
            file.write(f"{contador} : {blocker}\n")

    elif option == "2":
        if os.path.getsize("database.txt") == 0:
            print("The database is empty\n")
            input("Press enter to continue...")
        else:
            with open ("database.txt", "r") as file:

                for line in file:
                    print(f"{line.strip()}")
            input("Press enter to continue...")
    
    elif option == "3":
        with open("database.txt", "w") as archivo:
            pass 
        print("The database was cleaned correctly\n")
        input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif option == "4":
        break

    elif option == "exit":
        break
    
    else:
        print("Invalid option\n")