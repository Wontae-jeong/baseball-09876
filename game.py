class Game:
    def guess(self, guess_number):
        if guess_number is None:
            raise TypeError()

        if len(guess_number) != 3:
            raise TypeError()

        for number in guess_number:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()

        if (guess_number[0] == guess_number[1] or
                guess_number[0] == guess_number[2] or
                guess_number[1] == guess_number[2]):
            raise TypeError()
