from unittest import TestCase

from game.validator.InvalidWordReason import InvalidWordReason
from game.validator.WordleValidaor import WordleValidator


class TestWordleValidator(TestCase):
    def test_should_return_non_alpha(self):
        word = '12345'
        wordle_validator = WordleValidator()
        result = wordle_validator.validate(word)
        self.assertEqual(InvalidWordReason.NOT_ALPHA.value, result[0].value)

