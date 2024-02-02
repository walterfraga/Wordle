from unittest import TestCase
from unittest.mock import Mock, MagicMock

from game.WordleGame import WordleGame
from game.evaluator.Hint import Hint
from game.model.Guess import Guess
from game.validator.InvalidWordReason import InvalidWordReason
from game.validator.WordleValidaor import WordleValidator


class TestWordleGame(TestCase):

    def test_should_identify_chosen_word_as_invalid(self):
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
        self.assertIsNone(result.hints)

    def test_should_identify_chosen_word_as_expired(self):
        # given
        guess_word = 'words'
        validator = WordleValidator()
        validator.validate = MagicMock(return_value=None)
        evaluator = Mock()
        word_picker = Mock()
        wordle_game = WordleGame(0, word_picker, validator, evaluator)

        # when
        result = wordle_game.is_chosen_word(guess_word)

        # then
        self.assertEqual(Guess.EXPIRED.value, result.guess.value)
        self.assertIsNone(result.invalid_reasons)
        self.assertIsNone(result.hints)

    def test_should_identify_chosen_word_as_correct(self):
        # given
        guess_word = 'words'
        validator = WordleValidator()
        validator.validate = MagicMock(return_value=None)
        evaluator = Mock()
        word_picker = Mock()
        word_picker.pick_word = MagicMock(return_value=guess_word)
        wordle_game = WordleGame(1, word_picker, validator, evaluator)

        # when
        result = wordle_game.is_chosen_word(guess_word)

        # then
        self.assertEqual(Guess.CORRECT.value, result.guess.value)
        self.assertIsNone(result.invalid_reasons)
        self.assertIsNone(result.hints)

    def test_should_identify_chosen_word_as_incorrect(self):
        # given
        guess_word = 'words'
        validator = WordleValidator()
        validator.validate = MagicMock(return_value=None)
        evaluator = Mock()
        hints = [dict(letter='', hint=Hint.CORRECT_PLACE)]
        evaluator.evaluate = MagicMock(return_value=hints)
        word_picker = Mock()
        wordle_game = WordleGame(1, word_picker, validator, evaluator)

        # when
        result = wordle_game.is_chosen_word(guess_word)

        # then
        self.assertEqual(Guess.INCORRECT.value, result.guess.value)
        self.assertIsNone(result.invalid_reasons)
        self.assertEqual(hints, result.hints)