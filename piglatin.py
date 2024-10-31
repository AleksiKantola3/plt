from piglatin_error import PigLatinError

class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase if phrase else "nil"
        self.allowed_punctuations = [".", ",", ";", ":", "'", "!", "?", "(", ")"]

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self):
        if self.phrase == "nil":
            pass
        elif ' ' in self.phrase:
            words = self.phrase.split()
            translated_words = [self.translate_single_word(word) for word in words]
            self.phrase = ' '.join(translated_words)
        else:
            self.phrase = self.translate_single_word(self.phrase)

    def translate_single_word(self, word: str) -> str:
        container = ""
        if '-' in word:
            parts = word.split('-')
            translated_parts = [self.translate_single_word(part) for part in parts]
            return '-'.join(translated_parts)
        if not word[-1].isalpha():
            if word[-1] in self.allowed_punctuations:
                container = word[-1]
                word = word[:-1]
                word = self.translate_single_word(word)
                return word + container
            else:
                raise PigLatinError
        elif word[0] in 'aeiou':
            if word[-1] == 'y':
                return word + 'nay'
            elif word[-1] in 'aeiou':
                return word + 'yay'
            else:
                return word + 'ay'
        else:
            first_vowel_idx = next((i for i, char in enumerate(word) if char in 'aeiou'), None)
            if first_vowel_idx is not None and first_vowel_idx > 0:
                return word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay'
            else:
                return word + 'ay'

