def first(hello):
    return hello


def feature(params):
    return 5


def now_i(parmas):
    return 6

def branch_conflict_function(param):
    return param + 2

class TestingConflict():
    """Trying something new
    """

    def __init__(self):
        self.data = "Hello world"

    def function_first(self):
        return self.data + "main"

    def function_second(self):
        return self.data + "branch-a"

    def function_third(self):
        return self.data + "b"