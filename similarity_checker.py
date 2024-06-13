class SimilarityChecker:
    def check_similarity(self, str_a, str_b):
        if str_a is None or str_b is None:
            raise TypeError()