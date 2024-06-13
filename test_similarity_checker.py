from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestChecker(TestCase):
    def setUp(self):
        self.checker = SimilarityChecker()
        super().setUp()

    def assert_score(self, str_a, str_b):
        self.assertEqual(60, self.checker.check_similarity(str_a, str_b))

    def test_exception_when_input_is_none(self):
        with self.assertRaises(TypeError):
            self.checker.check_similarity()

    def test_exception_when_input_length_is_zero(self):
        with self.assertRaises(TypeError):
            self.checker.check_similarity("", "")

    def test_similarity_of_same_input_length(self):
        self.assert_score("asdaf", "asdee")


    def test_similarity_of_longer_than_twice_length(self):
        self.assertEqual(0, self.checker.check_similarity("aaf", "a112sdee"))
