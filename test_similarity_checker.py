from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestChecker(TestCase):
    def setUp(self):
        self.checker = SimilarityChecker()
        super().setUp()

    def test_exception_when_input_is_none(self):
        with self.assertRaises(TypeError):
            self.checker.check_similarity()

    def test_exception_when_input_length_is_zero(self):
        with self.assertRaises(TypeError):
            self.checker.check_similarity("", "")

    def test_similarity_of_same_input_length(self):
        self.assertEqual(60, self.checker.check_similarity("asdaf", "asdee"))
