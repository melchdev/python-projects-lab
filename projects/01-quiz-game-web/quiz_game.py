import json
import random
import unicodedata

# cd projects/01-quiz-game-web
# python quiz_game.py

# This function loads the questions from the questions.json file
def load_questions():

    with open ("./questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)

    return questions

# This function takes by default five random questions to ask the player
def get_random_questions(questions, num_of_questions=5):
    selected_questions = random.sample(questions, num_of_questions)
    return selected_questions

# Help of chatico :p
# This function normalizes the user's and real answers to verify if the user answered... 
# ...correctly regardless punctuation marks, extra spaces, etc.
def remove_accents(text):
    normalized_text = " ".join(text.strip().lower().split())

    normalized_text = unicodedata.normalize("NFD", normalized_text)

    text_without_accents = "".join(
        char for char in normalized_text
        if unicodedata.category(char) != "Mn"
    )
    return text_without_accents

def ask_question(question):

    user_answer=input(f"{question['question']} ")

    # Normalizing both the User's Answer and the Actual Answer
    user_answer = remove_accents(user_answer)
    actual_answer = remove_accents(question["answer"])

    well_answered = user_answer == actual_answer

    if well_answered:
        print("Yes! That's the answer")
    else:
        print("Incorrect. The answer was:", question["answer"])

    return well_answered

def run_quiz(playing):

    questions= load_questions()
    while playing:

        sample_questions = get_random_questions(questions)
        points = 0

        print("------GAME STARTED------")

        for index, question in enumerate(sample_questions, start=1):
            print(f"{index}. ", end='') 
            if ask_question(question):
                points +=1

        print("------GAME FINISHED------")
        match points:
            case 0:
                print(f"You got {points} ponits :c. You might take History lessons")
            case 1:
                print(f"You have {points} point. It's better than zero")
            case 2:
                print(f"You got {points} points! You are a little genius. Aren't you?")
            case 3:
                print(f"You've obtain {points} points. What a nerd")
            case 4:
                print(f"You have {points} points. You know pretty much about History")
            case 5:
                print(f"{points} points!. Perfect score!")
            case _:
                print("Why are we here?")
        play_again = input("Do you want to play again? Write \'yes\' ")
        play_again = remove_accents(play_again)

        if play_again == 'yes':
            print("Great! Let's do another round")
        else:
            playing = False
        

print("Welcome to my History Quiz!")
playing = input("Do you want to play? Write \'Yes\' ")
playing = remove_accents(playing)

# TODO show score of player after ending each game 

if playing == 'yes':

    print("Okay! Let's get started")
    run_quiz(True)

print("Goodbye! :D")