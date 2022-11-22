import random


class QuizBrain:
    def __init__(self, list, players):
        self.questions_list = list
        self.score = 0
        self.players = players

    def has_winner(self):
        final_score = 2
        winners = 0
        for player in self.players:
            if player.score == final_score:
                winners += 1
        if winners >= 2:
            final_score += 1
            winners = 0
            print(
                f"It's a tie! To win one must get {final_score} points alone now!")
        for player in self.players:
            if player.score == final_score:
                self.check_winner()
                return True

    def check_answer(self, player, guess, correct):
        if guess.lower() == correct.lower():
            print("You got it right!")
            player.score += 1
        else:
            print("That's wrong :/")
        print(f"The correct answer is {correct}")
        print(
            f"{player.name}'s current score is {player.score}")
        print("\n")

    def next_question(self, player):
        player_in_turn = player
        get_question = self.questions_list[random.randint(
            0, len(self.questions_list) - 1)]
        print(
            f"question for {player_in_turn.name}: ({get_question.category}) {get_question.question} True or False?")
        guess = input()
        self.check_answer(player_in_turn, guess, get_question.correct_answer)

    def players_rotation(self):
        for player in self.players:
            self.next_question(player)

    def check_winner(self):
        winner = {}
        for player in self.players:
            print(player.name, player.score)
            if not winner or player.score > winner.score:
                winner = player
        print(f"The winner is {winner.name} with {winner.score} points")
