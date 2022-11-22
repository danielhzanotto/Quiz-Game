from question_model import Question
from data import game_data
from quiz_brain import QuizBrain
from player import Player


players = []
question_bank = []
question_data = game_data
quiz_brain = QuizBrain(question_bank, players)


for d in question_data:
    question_text = d["question"]
    question_answer = d["correct_answer"]
    question_category = d["category"]
    question_difficulty = d["difficulty"]
    new_question = Question(
        question_text, question_answer, question_category, question_difficulty)
    question_bank.append(new_question)


add = "y"
while add == "y":
    player = Player(input("Please type the player's name:").capitalize())
    players.append(player)
    add = input("Would you like to add another player? Y/N").lower()


while not quiz_brain.has_winner():
    quiz_brain.players_rotation()
