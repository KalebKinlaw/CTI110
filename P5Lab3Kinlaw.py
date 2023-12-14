"""
Kaleb Kinlaw
CTI - 110 
P5Lab 3 - Quiz Show 
11/7/23
"""

question_set = [
    {
        "question": "What was the popular dance move in the 1980s?",
        "choices": ["The twist", "The moonwalk", "The electric slide"],
        "answer": 1
    },
    {
        "question": "Which band had a hit song called 'Like a Prayer'?",
        "choices": ["Madonna", "Michael Jackson", "Prince"],
        "answer": 0
    },
    {
        "question": "Who starred as Marty McFly in the movie 'Back to the Future'?",
        "choices": ["Tom Cruise", "Michael J. Fox", "Leonardo DiCaprio"],
        "answer": 1
    }
]
score = 0
def ask_question(question_obj):
    global score
    print(question_obj["question"])
    choices = question_obj["choices"]
    for i in range(len(choices)):
        print(f"{i+1}. {choices[i]}")
    user_answer = int(input("Enter your answer (1-3): "))
    if user_answer - 1 == question_obj["answer"]:
        score += 1

for question in question_set:
    ask_question(question)

print("Your score: ", score)