class SimilarityChecker:
    def check_similarity(self, str_a, str_b):
        self.assert_illegal_input(str_a, str_b)
        if len(str_a) == len(str_b):
            return 60

    def assert_illegal_input(self, str_a, str_b):
        if str_a is None or str_b is None:
            raise TypeError()
        if len(str_a) == 0 or len(str_b) == 0:
            raise TypeError()
