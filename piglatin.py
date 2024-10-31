
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase if phrase else "nil"

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self):
        if self.phrase == "nil":
            pass
        elif self.phrase[0] in 'aeiou':
            if self.phrase[-1] == 'y':
                self.phrase += 'nay'
            elif self.phrase[-1] in 'aeiou':
                self.phrase += 'yay'
            else:
                self.phrase += 'ay'
        else:
            first_vowel_idx = next((i for i, char in enumerate(self.phrase) if char in 'aeiou'), None)
            if first_vowel_idx is not None and first_vowel_idx > 0:
                self.phrase = self.phrase[first_vowel_idx:] + self.phrase[:first_vowel_idx] + 'ay'
            else:
                self.phrase += 'ay'

