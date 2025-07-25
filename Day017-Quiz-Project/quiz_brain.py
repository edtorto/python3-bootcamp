import random
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list  = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < 10

    def next_question(self):
        """Retrieve the item at the current question number.from the question list."""
        question_num = random.randint(1, len(self.question_list))
        question = self.question_list[question_num]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right! {correct_answer}")
        else:
            print("You got it wrong!")
        print(f"The correct answer: {correct_answer}")
        print(f"Score : {self.score}/{self.question_number} \n")