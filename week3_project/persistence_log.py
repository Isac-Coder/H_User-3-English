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
    print("\nWrite to exit to close the program")
    blocker = input("\nEnter your daily blocker:\n# ")

    if blocker.lower() == "exit":
        break

    contador += 1

    with open ("database.txt", "a") as file:
        
        file.write(f"{contador} : {blocker}\n")

    with open ("database.txt", "r") as file:
        for line in file:
            print(f"{line.strip()}")
    
    # Opción rápida: el archivo se abre y se cierra inmediatamente, quedando vacío
    with open("tu_archivo.txt", "w") as archivo:
        pass 

