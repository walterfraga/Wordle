import unittest
from game.validator.InvalidWordReason import InvalidWordReason
from game.validator.WordleValidaor import WordleValidator


class TestWordleValidator(unittest.TestCase):

    def test_should_return_none_when_word_is_none(self):
        word = None
        wordle_validator = WordleValidator()
        result = wordle_validator.validate(word)
        self.assertEqual(None, result)

    def test_should_return_invalid_length_when_word_is_empty(self):
        word = ''
        wordle_validator = WordleValidator()
        result = wordle_validator.validate(word)
        self.assertEqual(InvalidWordReason.INVALID_LENGTH.value, result[0].value)

    def test_should_return_invalid_length_when_word_is_shorted_than_five_and_alpha(self):
        word = 'qa'
        wordle_validator = WordleValidator()
        result = wordle_validator.validate(word)
        self.assertEqual(InvalidWordReason.INVALID_LENGTH.value, result[0].value)

    def test_should_return_non_alpha(self):
        word = '12345'
        wordle_validator = WordleValidator()
        result = wordle_validator.validate(word)
        self.assertEqual(1, len(result))
        self.assertEqual(InvalidWordReason.NOT_ALPHA.value, result[0].value)

    def test_should_return_non_alpha_and_invalid_length_when_word_in_non_numeric_and_shorter_than_5(self):
        word = '1234'
        wordle_validator = WordleValidator()
        result = wordle_validator.validate(word)
        self.assertEqual(2, len(result))
        self.assertEqual(InvalidWordReason.INVALID_LENGTH.value, result[0].value)
        self.assertEqual(InvalidWordReason.NOT_ALPHA.value, result[1].value)


if __name__ == '__main__':
    unittest.main()
