# programmed by @ezthalisson
# 20/12/2021

# imports
from random import randint as rdt


class Game:
    def __init__(self):
        self.kick = None
        self.dado = None
        self.run = True
        self.attempts = 0

    def main(self):
        self.generator()

        while self.run:
            self.question()
            self.checker()

    def generator(self):
        self.dado = rdt(1, 6)

    def question(self):
        try:
            self.kick = int(input('What number do you guess? '))

            if self.kick > 6 or self.kick <= 0:
                print('Please enter only a number from 1 to 6!')
                self.question()

        except ValueError:
            print('Wrong value! Try again.')
            self.question()

    def message_welcome(self):
        print('=' * 40)
        print('Welcome! Guess a number from 1 to 6.')
        print('=' * 40)

    def checker(self):
        if self.kick == self.dado:
            self.attempts += 1
            self.message_win()
            self.play_again()
        if self.kick > self.dado:
            self.attempts += 1
            print('Try a smaller number!')
        if self.kick < self.dado:
            self.attempts += 1
            print('Try a bigger number!')

    def message_win(self):
        print('=' * 40)
        print(f'Congratulations! You got it right in {self.attempts} attempts.')
        print('=' * 40)

    def play_again(self):
        try:
            answer = str(input('Play again? ')).upper().strip()[0]

            if answer == 'Y':
                self.attempts = 0
                self.main()
            elif answer == 'N':
                self.run = False
                print('=' * 40)
                print('Thank you for participating! Check back often.')
                print('=' * 40)
            elif not answer in 'YN':
                print('Please just say yes or no!')
                self.play_again()
        except ValueError:
            print('Please just say yes or no!')
            self.play_again()


if __name__ == '__main__':
    game = Game()
    game.message_welcome()
    game.main()
