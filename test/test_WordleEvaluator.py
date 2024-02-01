import unittest

from game.evaluator.Hint import Hint
from game.evaluator.WordleEvaluator import WordleEvaluator


class TestWordleEvaluator(unittest.TestCase):

    def test_should_return_none_when_none(self):
        wordle_evaluator = WordleEvaluator()
        result = wordle_evaluator.evaluate('w', None)
        self.assertIsNone(result)

    def test_should_return_none_when_empty(self):
        wordle_evaluator = WordleEvaluator()
        result = wordle_evaluator.evaluate('w', '')
        self.assertIsNone(result)

    def test_should_return_correct_place_for_single_letter(self):
        wordle_evaluator = WordleEvaluator()
        result = wordle_evaluator.evaluate('w', 'w')
        self.assertEqual(1, len(result))
        self.assertEqual('w', result[0]['letter'])
        self.assertEqual(Hint.CORRECT_PLACE.value, result[0]['hint'].value)

    def test_should_return_not_in_word_for_single_letter(self):
        wordle_evaluator = WordleEvaluator()
        result = wordle_evaluator.evaluate('w', 'x')
        self.assertEqual(1, len(result))
        self.assertEqual('x', result[0]['letter'])
        self.assertEqual(Hint.NOT_IN_WORD.value, result[0]['hint'].value)

    def test_should_return_not_in_word_and_within_word(self):
        wordle_evaluator = WordleEvaluator()
        result = wordle_evaluator.evaluate('words', 'xw')
        self.assertEqual(2, len(result))
        self.assertEqual('x', result[0]['letter'])
        self.assertEqual(Hint.NOT_IN_WORD.value, result[0]['hint'].value)
        self.assertEqual('w', result[1]['letter'])
        self.assertEqual(Hint.WITHIN_WORD.value, result[1]['hint'].value)

    def test_should_return_within_word_correct_place_not_in_word(self):
        wordle_evaluator = WordleEvaluator()
        result = wordle_evaluator.evaluate('words', 'sdrox')
        self.assertEqual(5, len(result))
        self.assertEqual('s', result[0]['letter'])
        self.assertEqual(Hint.WITHIN_WORD.value, result[0]['hint'].value)
        self.assertEqual('d', result[1]['letter'])
        self.assertEqual(Hint.WITHIN_WORD.value, result[1]['hint'].value)
        self.assertEqual('r', result[2]['letter'])
        self.assertEqual(Hint.CORRECT_PLACE.value, result[2]['hint'].value)
        self.assertEqual('o', result[3]['letter'])
        self.assertEqual(Hint.WITHIN_WORD.value, result[3]['hint'].value)
        self.assertEqual('x', result[4]['letter'])
        self.assertEqual(Hint.NOT_IN_WORD.value, result[4]['hint'].value)


if __name__ == '__main__':
    unittest.main()
