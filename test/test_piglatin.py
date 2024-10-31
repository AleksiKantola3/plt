import unittest

import piglatin
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phrase(self):
        phrase = "hello world"
        translator = PigLatin(phrase)
        self.assertEqual(phrase, translator.get_phrase())


    def test_input_empty_phrase(self):
        phrase = ""
        translator = PigLatin(phrase)
        self.assertEqual("nil", translator.get_phrase())


    def test_translate_phrase_starts_with_vowel_ends_in_y(self):
        phrase = "any"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("anynay", translator.get_phrase())


    def test_translate_phrase_starts_with_vowel_ends_in_vowel_not_y(self):
        phrase = "apple"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("appleyay", translator.get_phrase())

    def test_translate_phrase_starts_with_vowel_ends_in_consonant(self):
        phrase = "ask"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("askay", translator.get_phrase())

    def test_translate_phrase_starts_with_consonant(self):
        phrase = "hello"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("ellohay", translator.get_phrase())

    def test_translate_phrase_starts_with_more_than_one_consonant(self):
        phrase = "known"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("ownknay", translator.get_phrase())

    def test_translate_phrase_with_more_words(self):
        phrase = "hello world"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("ellohay orldway", translator.get_phrase())


    def test_translate_phrase_with_composite_word(self):
        phrase = "well-being"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("ellway-eingbay", translator.get_phrase())


    def test_translate_phrase_with_more_words_and_punctuations(self):
        phrase = "hello world!"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("ellohay orldway!", translator.get_phrase())