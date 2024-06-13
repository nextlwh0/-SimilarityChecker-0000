class SimilarityChecker:
    def check_similarity(self, str_a, str_b):
        if str_a is None or str_b is None:
            raise TypeError()
        if len(str_a)==0 or len(str_b)==0:
            raise TypeError()