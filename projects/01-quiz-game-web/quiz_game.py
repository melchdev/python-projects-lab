print("Welcome to my History Quiz!")

playing = input("Do you want to play my game? ")

if playing != "yes":
    quit()

print("Nice! Let's play then")

guess = input("What is the capital of France? ")

answer = "Paris"

if guess == answer:
    print("You nailed it! The city of love")