from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestChcker(TestCase):
    def test_exception_when_input_is_none(self):
        self.checker = SimilarityChecker()
        with self.assertRaises(TypeError):
            self.checker.check_similarity()