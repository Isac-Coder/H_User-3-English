import os

if os.path.exists("database.txt"):
    pass
else:
    with open ("database.txt", "w") as file:
        pass

with open("database.txt", "r") as file:
    contador = len(file.readlines())

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    option = int(input("Enter an option:\n#"))
    os.system('cls' if os.name == 'nt' else 'clear')

    if option == 1:
        print("\nWrite to exit to close the program")
        blocker = input("\nEnter your daily blocker:\n# ")
        contador += 1
        with open ("database.txt", "a") as file:
            file.write(f"{contador} : {blocker}\n")

    elif option == 2:
        with open ("database.txt", "r") as file:
            for line in file:
                print(f"{line.strip()}")
        print("\nWrite to exit to close the program")
    
    elif option == 3:
        with open("database.txt", "w") as archivo:
            pass 
        print("The database was cleaned correctly\n")
        input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif option == 4:
        break