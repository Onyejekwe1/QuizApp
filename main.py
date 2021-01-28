from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

bank = []
for question in question_data:
    question_obj = Question(question['question'], question['correct_answer'])
    bank.append(question_obj)

quiz = QuizBrain(bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz, your final score was {quiz.score}/{quiz.question_number}")
