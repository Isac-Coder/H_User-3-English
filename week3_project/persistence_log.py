import os

if os.path.exists("database.txt"):
    pass
else:
    with open ("database.txt", "w") as file:
        pass

with open("database.txt", "r") as file:
    contador = len(file.readlines())

os.system("cls")
while True:
    print("Write to exit to close the program")
    blocker = input("Enter your daily blocker:\n# ")

    if blocker.lower() == "exit":
        break

    contador += 1

    with open ("database.txt", "a") as file:
        
        file.write(f"{contador} : {blocker}\n")

    with open ("database.txt", "r") as file:
        for line in file:
            print(f"{line.strip()}")
