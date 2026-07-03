'''TODO: NúmeroPregunta - hacer pregunta (verdadero o falso)
        confirmar
        indicar respuesta correcta
        marcar puntuación
'''
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(text=data["question"], answer=data["correct_answer"]) for data in question_data]
quiz = QuizBrain(question_bank)

play = True
while play == True:
        quiz.next_question()

        play = quiz.still_has_questions()

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")
        
