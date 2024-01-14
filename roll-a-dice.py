import random

while True:
    rolldice = input("Do you want to roll the dice? (y/n): ")
    
    if rolldice == "y":
        print(random.randint(1, 6))
    else:
        print("Exiting the dice rolling program.")
        break
