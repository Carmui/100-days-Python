class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        curr_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False): ")
        self.check_answer(user_answer, curr_question.answer)

    def still_has_questions(self):
        return len(self.questions_list) > self.question_number

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print(f"Current score: {self.score}/{self.question_number}")
        else:
            print(f"Wrong answer, your score: {self.score}/{self.question_number}")

        print(f"The correct answer: {correct_ans}")
