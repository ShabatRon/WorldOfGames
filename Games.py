class Game:
    def __init__(self, name):
        self.name = name
        self.welcome_line = f"\nHello {self.name} and welcome to the World of Games!!! \nHere you can find many cool games to play."
        self.menu_text = """
Please choose a game to play: \n
  1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
  2. Guess Game - guess a number and see if you chose like the computer
  3. Currency Roulette - try and guess the value of a random amount of USD in ILS
"""
        self.selected_number = 1
        self.selected_difficulty = 1
        print(self.welcome_line)

    def load_game(self):
        self.selected_number = input(self.menu_text)
        # Input validation:
        while True:
            if not self.selected_number.isnumeric() or not int(self.selected_number) in (1, 2, 3):
                print("########\nyour input is invalid!!\n########\n\n")
                self.selected_number = input(self.menu_text)
            else:
                break

        self.selected_difficulty = input("Please choose a game difficulty from 1 to 5:")
        # Input validation:
        while True:
            if not self.selected_difficulty.isnumeric() or not int(self.selected_difficulty) in (1, 2, 3, 4, 5):
                print("########\nyour input is invalid!!\n########\n\n")
                self.selected_difficulty = input("Please choose a game difficulty from 1 to 5:")
            else:
                break

        print(f"Selected game is: {self.selected_number} , selected difficulty is: {self.selected_difficulty}")
        return self.selected_difficulty, self.selected_difficulty




