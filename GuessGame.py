from random import randint
from Games import Game

class GuessGame(Game):
    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.guess_number = 0
        self.secret_number = 0
        self.ans = True
        # data = {
        #    "Game_name": "GuessGame",
        #    "difficulty": self.difficulty
        # }
        # super().__init__(**data)

    def generate_secret_number(self):
        """
        Generate a random number between 1 to <difficulty> and save it to secret_number
        """
        self.secret_number = randint(0, self.difficulty)
        # print(f"secret_number = {self.secret_number}")

    def get_guess_from_user(self):
        """
        Prompt the user for a number between 1 to <difficulty> and return the number.
        :return: User's selected number
        """
        self.guess_number = input(f"please guess a number between 1 to {self.difficulty}:  \n")
        while True:
            if not self.guess_number.isnumeric() or \
                    not int(self.guess_number) <= self.difficulty or \
                    not int(self.guess_number) >= 0:
                self.guess_number = input(f"you input is invalid!! please guess a number between 1 to {self.difficulty}:  \n")
            else:
                self.guess_number = int(self.guess_number)
                break
        return self.guess_number

    def compare_results(self):
        """
        # compare_results - Will compare the the secret generated number to the one prompted
        # by the get_guess_from_user.
        """
        return self.guess_number == self.secret_number

    def play(self):
        """
        play - Will call the functions above and play the game.
        :return:Will return True / False if the user lost or won.
        """
        print("Game is starting!!")
        self.generate_secret_number()
        while True:
            self.get_guess_from_user()
            self.ans = self.compare_results()
            if self.ans:
                print(f"Right Guess!! , the number is {self.secret_number}")
                break
            else:
                print(f"Wrong Guess!! , Please try again.")
        return self.ans


run = GuessGame(5)
run.play()

