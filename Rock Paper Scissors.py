import os


def cls():
    os.system("CLS")


class Game:

    def __init__(self, first_player_name, second_player_name):

        self.first_player_name = first_player_name

        self.second_player_name = second_player_name

    def play(self):
        first_player_count = 0
        second_player_count = 0
        while True:

            moves = [" ", " "]
            while True:
                moves[0] = input(
                    f'Hello {self.first_player_name}! what is your choice? Rock Paper or Scissors?\n').lower()
                if moves[0] == "rock" or moves[0] == "paper" or moves[0] == "scissors":
                    break
                print("Wrong choice silly!")
            cls()
            while True:
                moves[1] = input(
                    f'Hello {self.second_player_name}! what is your choice? Rock Paper or Scissors?\n').lower()
                if moves[1] == "rock" or moves[1] == "paper" or moves[1] == "scissors":
                    break
                print("Wrong choice silly!")
            cls()
            for move in moves:

                if move == "rock":

                    print("""

                            _______

                        ---'   ____)

                              (_____)

                              (_____)

                              (____)

                        ---.__(___)

                        """)

                elif move == "paper":

                    print("""

                             _______

                        ---'    ____)____

                                   ______)

                                  _______)

                                 _______)

                        ---.__________)

                        """)

                else:

                    print("""

                            _______

                        ---'   ____)____

                                  ______)

                               __________)

                              (____)

                        ---.__(___)

                        """)
            if moves[0] == moves[1]:
                print("It is a tie!")
            elif ((moves[0] == "rock" and moves[1] == "scissors")
                  or (moves[0] == "scissors" and moves[1] == "paper")
                  or (moves[0] == "paper" and moves[1] == "rock")):
                print(f"Well done {self.first_player_name} you won!")
                first_player_count = first_player_count + 1
            else:
                print(f'Well done {self.second_player_name} you won!')
                second_player_count = second_player_count + 1
            print(
                f"The Score is : {self.first_player_name} {first_player_count} - {self.second_player_name} {second_player_count}")
            answer = input("Would you like to play again? Y/N\n")
            answer = answer.lower()
            if not (answer == "y" or answer == "yes"):
                break
        print("Good Bye!!!")


if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors game!")
    player1_name = input("Write the name of the first player: ")
    player2_name = input("Write the name of the second player: ")
    cls()
    game = Game(player1_name, player2_name)

    game.play()
