import unittest

from game.evaluator.Hint import Hint
from game.evaluator.WordleEvaluator import WordleEvaluator


class TestWordleEvaluator(unittest.TestCase):

    def setUp(self):
        self.chosen_word = 'words'
        self.wordle_evaluator = WordleEvaluator()

    def test_should_return_none_when_none(self):
        result = self.wordle_evaluator.evaluate(self.chosen_word, None)
        self.assertIsNone(result)

    def test_should_return_none_when_empty(self):
        result = self.wordle_evaluator.evaluate(self.chosen_word, '')
        self.assertIsNone(result)

    def test_should_return_correct_place_for_single_letter(self):
        result = self.wordle_evaluator.evaluate(self.chosen_word, 'w')
        self.assertEqual(1, len(result))
        self.assertEqual('w', result[0]['letter'])
        self.assertEqual(Hint.CORRECT_PLACE.value, result[0]['hint'].value)

    def test_should_return_not_in_word_for_single_letter(self):
        result = self.wordle_evaluator.evaluate(self.chosen_word, 'x')
        self.assertEqual(1, len(result))
        self.assertEqual('x', result[0]['letter'])
        self.assertEqual(Hint.NOT_IN_WORD.value, result[0]['hint'].value)

    def test_should_return_not_in_word_and_within_word(self):
        result = self.wordle_evaluator.evaluate(self.chosen_word, 'xw')
        self.assertEqual(2, len(result))
        self.assertEqual('x', result[0]['letter'])
        self.assertEqual(Hint.NOT_IN_WORD.value, result[0]['hint'].value)
        self.assertEqual('w', result[1]['letter'])
        self.assertEqual(Hint.WITHIN_WORD.value, result[1]['hint'].value)

    def test_should_return_within_word_correct_place_not_in_word(self):
        result = self.wordle_evaluator.evaluate(self.chosen_word, 'sdrox')
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
