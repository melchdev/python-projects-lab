import json
import random
import unicodedata

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
def remove_accents(text):
    normalized_text = unicodedata.normalize("NFD", text)
    text_without_accents = "".join(
        char for char in normalized_text
        if unicodedata.category(char) != "Mn"
    )
    return text_without_accents

# This function normalizes the user's and real answers to verify if the user answered... 
# ...correctly regardless punctuation marks, extra spaces, etc.
def check_answer(user_answer, actual_answer):
    norm_user_answer = " ".join(user_answer.strip().lower().split())
    norm_user_answer = remove_accents(norm_user_answer)
    
    norm_actual_answer = " ".join(actual_answer.strip().lower().split())
    norm_actual_answer = remove_accents(norm_actual_answer)

    return norm_user_answer == norm_actual_answer

def ask_question(question):

    user_answer=input(f"{question['question']} ")

    well_answered = check_answer(user_answer, question["answer"])

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

        for index, question in enumerate(sample_questions, start=1):
            print(f"{index}. ", end='') 
            if ask_question(question):
                points +=1

        play_again = int(input("Do you want to play again?\n Write \'yes\' "))
        play_again = " ".join(play_again.strip().lower().split())
        play_again = remove_accents(play_again)

        if not play_again:
            playing = False

print("Welcome to my History Quiz!")
playing = input("Do you want to play? Write \'yes\' ")
playing = " ".join(playing.strip().lower().split())
playing = remove_accents(playing)

# TODO validate user input, show score of player after ending each game 

# TODO restructure check_answer to make an universal function to remove spaces en make it lowercase

if playing == 'yes':

    print("Okay! Let's get started")
    run_quiz(playing)

print("Goodbye! :D")