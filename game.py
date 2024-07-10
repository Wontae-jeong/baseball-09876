from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guess_number) -> GameResult:
        self.assert_illegal_value(guess_number)
        if guess_number == self.question:
            return GameResult(True, 3, 0)

        else:
            strikes = 0
            balls = 0
            for i in range(len(guess_number)):
                if self.question.find(guess_number[i]) == i:
                    strikes += 1
                elif self.question.find(guess_number[i]) > -1:
                    balls += 1
            return GameResult(False, strikes, balls)

    def assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError()
        if len(guess_number) != 3:
            raise TypeError()
        for number in guess_number:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self.has_duplicated_number(guess_number):
            raise TypeError()

    def has_duplicated_number(self, guess_number):
        return (guess_number[0] == guess_number[1] or
                guess_number[0] == guess_number[2] or
                guess_number[1] == guess_number[2])
