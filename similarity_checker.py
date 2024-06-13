class SimilarityChecker:
    def check_similarity(self, str_a, str_b):
        self.assert_illegal_input(str_a, str_b)
        if self.is_same_length(str_a, str_b):
            return 60
        if self.is_longer_than_twice_length(str_a, str_b):
            return 0
        if len(str_a)>len(str_b):
            gap = len(str_a) - len(str_b)
            return (1-gap/len(str_b))*60
        else:
            gap = len(str_b) - len(str_a)
            return (1-gap/len(str_a))*60


    def is_longer_than_twice_length(self, str_a, str_b):
        return 2*len(str_a) <= len(str_b) or len(str_a) >= 2*len(str_b)

    def is_same_length(self, str_a, str_b):
        return len(str_a) == len(str_b)

    def assert_illegal_input(self, str_a, str_b):
        if str_a is None or str_b is None:
            raise TypeError()
        if len(str_a) == 0 or len(str_b) == 0:
            raise TypeError()
