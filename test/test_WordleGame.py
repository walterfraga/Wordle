from unittest import TestCase
from unittest.mock import Mock, MagicMock

from game.WordleGame import WordleGame
from game.model.Guess import Guess
from game.validator.InvalidWordReason import InvalidWordReason
from game.validator.WordleValidaor import WordleValidator


class TestWordleGame(TestCase):

    def test_is_chosen_word(self):
        # given
        guess_word = 'words'
        invalid_reasons = [InvalidWordReason.INVALID_LENGTH]
        validator = WordleValidator()
        validator.validate = MagicMock(return_value=invalid_reasons)
        evaluator = Mock()
        word_picker = Mock()

        wordle_game = WordleGame(1, word_picker, validator, evaluator)

        # when
        result = wordle_game.is_chosen_word(guess_word)

        # then
        self.assertEqual(Guess.INVALID.value, result.guess.value)
        self.assertEqual(invalid_reasons, result.invalid_reasons)
