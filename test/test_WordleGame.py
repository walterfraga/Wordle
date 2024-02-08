from unittest import TestCase
from unittest.mock import Mock, MagicMock

from game.WordleGame import WordleGame
from game.evaluator.Hint import Hint
from game.model.Guess import Guess
from game.validator.InvalidWordReason import InvalidWordReason


class TestWordleGame(TestCase):

    def test_should_identify_chosen_word_as_invalid(self):
        # given
        guess_word = 'words'
        invalid_reasons = [InvalidWordReason.INVALID_LENGTH]
        validator = Mock()
        validator.validate = MagicMock(return_value=invalid_reasons)
        evaluator = Mock()

        wordle_game = WordleGame(1, "tests", validator, evaluator)

        # when
        result = wordle_game.is_chosen_word(guess_word)

        # then
        self.assertEqual(Guess.INVALID.value, result.guess.value)
        self.assertEqual(invalid_reasons, result.invalid_reasons)
        self.assertIsNone(result.hints)

    def test_should_identify_chosen_word_as_expired(self):
        # given
        guess_word = 'words'
        validator = Mock()
        validator.validate = MagicMock(return_value=None)
        evaluator = Mock()
        wordle_game = WordleGame(0, "ddddd", validator, evaluator)

        # when
        result = wordle_game.is_chosen_word(guess_word)

        # then
        self.assertEqual(Guess.EXPIRED.value, result.guess.value)
        self.assertIsNone(result.invalid_reasons)
        self.assertIsNone(result.hints)

    def test_should_identify_chosen_word_as_correct(self):
        # given
        guess_word = 'words'
        validator = Mock()
        validator.validate = MagicMock(return_value=None)
        evaluator = Mock()
        wordle_game = WordleGame(1, "words", validator, evaluator)

        # when
        result = wordle_game.is_chosen_word(guess_word)

        # then
        self.assertEqual(Guess.CORRECT.value, result.guess.value)
        self.assertIsNone(result.invalid_reasons)
        self.assertIsNone(result.hints)

    def test_should_identify_chosen_word_as_incorrect(self):
        # given
        guess_word = 'words'
        validator = Mock()
        validator.validate = MagicMock(return_value=None)
        evaluator = Mock()
        hints = [dict(letter='', hint=Hint.CORRECT_PLACE)]
        evaluator.evaluate = MagicMock(return_value=hints)
        wordle_game = WordleGame(1, "sdsds", validator, evaluator)

        # when
        result = wordle_game.is_chosen_word(guess_word)

        # then
        self.assertEqual(Guess.INCORRECT.value, result.guess.value)
        self.assertIsNone(result.invalid_reasons)
        self.assertEqual(hints, result.hints)

    def test_should_return_remaining_letters(self):
        # given
        guess_word = 'words'
        validator = Mock()
        validator.validate = MagicMock(return_value=None)
        evaluator = Mock()

        wordle_game = WordleGame(1, "words", validator, evaluator)

        # when
        wordle_game.is_chosen_word(guess_word)
        remaining_letters = wordle_game.get_remaining_letters()

        # then
        self.assertEqual('abc efghijklmn pq  tuv xyz', ''.join(remaining_letters))
