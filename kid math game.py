#simple math game for kids
#Lwazi Somtsewu

import random

def generate_question():
    # Randomly choose between addition and subtraction
    operation = random.choice(['+', '-'])
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    if operation == '+':
        answer = num1 + num2
        question = f"What is {num1} + {num2}?"
    else:
        answer = num1 - num2
        question = f"What is {num1} - {num2}?"

    return question, answer

def math_game():
    print("Welcome to the Math Game for Kids!")
    print("You will be asked a series of math questions.")
    print("Type 'exit' to end the game at any time.")
    
    score = 0
    total_questions = 5

    for _ in range(total_questions):
        question, answer = generate_question()
        print(question)
        
        user_input = input("Your answer: ")
        
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break
        
        try:
            user_answer = int(user_input)
        except ValueError:
            print("Please enter a valid number or type 'exit' to quit.")
            continue
        
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {answer}.")

    print(f"Game over! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    math_game()
