from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []


for question in question_data:
    text = question["text"]
    answer = question["answer"]

    question_object = Question(text, answer)

    question_list.append(question_object)

new_quiz = QuizBrain(question_list)

while new_quiz.still_has_questions():
     user_answ = new_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {new_quiz.score}/{len(question_list)}")