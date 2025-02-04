import random


class Generator:
    def __init__(self) -> None:
        self.letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    def random_number(self):
        return random.randint(2, 5)

    def generate_password(self):
        password = []

        while len(password) < 8:
            for list in [self.letters, self.numbers, self.symbols]:
                for _ in range(1, self.random_number()):
                    password.append(random.choice(list))

        random.shuffle(password)
        return "".join(password)
