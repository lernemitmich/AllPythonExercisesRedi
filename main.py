
print("Welcome to the game!")
#we first define a dictionary questions containing the quiz questions and answers
question= {
    
    "Which one is most populous country? " : "India", 
    "What is the capital of India?" : "New Delhi" , 
     "Who is the Prime Minister of India " : "Narendra Modi"}

# Now we will initialize score :
score = 0

# Now we will loop through the question, answers
for question, answer in question.items() :
    user_answer = input(question)
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# display score 
    print("Your score is:", score)
