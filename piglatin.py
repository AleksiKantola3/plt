
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase if phrase else "nil"

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self):
        if self.phrase[0] in 'aeiou':
            if self.phrase[-1] == 'y':
                self.phrase += 'nay'
            else:
                self.phrase += 'yay'

