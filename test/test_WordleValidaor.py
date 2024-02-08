import unittest
from game.validator.InvalidWordReason import InvalidWordReason
from game.validator.WordleValidaor import WordleValidator


class TestWordleValidator(unittest.TestCase):

    def setUp(self):
        self.wordle_validator = WordleValidator(5)

    def test_should_return_none_when_word_is_none(self):
        word = None
        result = self.wordle_validator.validate(word)
        self.assertEqual(None, result)

    def test_should_return_invalid_length_when_word_is_empty(self):
        word = ''
        result = self.wordle_validator.validate(word)
        self.assertEqual(InvalidWordReason.INVALID_LENGTH.value, result[0].value)

    def test_should_return_invalid_length_when_word_is_shorted_than_five_and_alpha(self):
        word = 'qa'
        result = self.wordle_validator.validate(word)
        self.assertEqual(InvalidWordReason.INVALID_LENGTH.value, result[0].value)

    def test_should_return_non_alpha(self):
        word = '12345'
        result = self.wordle_validator.validate(word)
        self.assertEqual(1, len(result))
        self.assertEqual(InvalidWordReason.NOT_ALPHA.value, result[0].value)

    def test_should_return_non_alpha_and_invalid_length_when_word_in_non_numeric_and_shorter_than_5(self):
        word = '1234'
        result = self.wordle_validator.validate(word)
        self.assertEqual(2, len(result))
        self.assertEqual(InvalidWordReason.INVALID_LENGTH.value, result[0].value)
        self.assertEqual(InvalidWordReason.NOT_ALPHA.value, result[1].value)

    def test_should_return_non_alpha_and_invalid_length_and_unknown_word_when_word_in_non_numeric_and_shorter_than_5_and_not_real_word(
            self):
        word = '1234'
        custom_wordle_validator = WordleValidator(5, ['nails'])
        result = custom_wordle_validator.validate(word)
        self.assertEqual(3, len(result))
        self.assertEqual(InvalidWordReason.INVALID_LENGTH.value, result[0].value)
        self.assertEqual(InvalidWordReason.NOT_ALPHA.value, result[1].value)
        self.assertEqual(InvalidWordReason.UNKNOWN_WORD.value, result[2].value)


if __name__ == '__main__':
    unittest.main()
