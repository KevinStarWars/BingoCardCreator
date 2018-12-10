import random


class WordExtractor:

    def __init__(self):
        self.word_list = [
            "Apple", "Bar Down", "Barnburner", "Bottle Rocket",
            "Breakaway", "Celly", "Cherry Picker", "Chiclets", "Chirp", "Clapper",
            "Coast To Coast", "Crossbar", "Dangle", "Dirty", "Duster", "Face Wash", "Filthy", "Fishbowl",
            "Five-Hole", "Flamingo", "Garbage", "Gino", "Gongshow", "Goon", "Grocery Stick",
            "Hands", "Hoser", "Junction", "Lettuce", "Light the Lamp", "Lumber", "Open ice Hit",
            "Pigeon", "Pipe", "Pinch", "Plug", "Point", "Pylon", "The Show", "Silky", "Stripes", "Sieve",
            "Sin-bin", "Slot", "Snipe", "Sweater", "Tape-to-Tape", "Tic Tac Toe", "Toe Drag", "Turtle",
            "Wheels", "Wraparound"
        ]
        self.content_words = [
            "Barn", "Beauty", "Twigs", "Flow", "Bender", "Man Rocket", "Cheese", "Bucket", "Filthy Mitts", "Saucers",
            "D Man", "Biscuit", "Grinders"
        ]

    def get_total_word_count(self):
        return len(self.word_list) + len(self.content_words)

    def get_content_word_count(self):
        return len(self.content_words)

    def check_discrete(self):
        tmp_list = []
        for c in self.content_words:
            if c in self.word_list:
                tmp_list.append(c)
        if len(tmp_list) == 0:
            return True
        else:
            print(tmp_list)
            return False

    def get_n_content_words(self, n):
        words = self.content_words
        chosen_words = []
        for i in range(n):
            picked_word = random.choice(words)
            chosen_words.append(picked_word)
            words.remove(picked_word)
        return chosen_words

    def get_n_words(self, n):
        words = self.word_list
        chosen_words = []
        for i in range(n):
            picked_word = random.choice(words)
            chosen_words.append(picked_word)
            words.remove(picked_word)
        return chosen_words