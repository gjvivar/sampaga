

class Sampaga:
    """
    Flower objects description

    Flower objects loneger description. (https://tl.wikipedia.org/wiki/Sampaga)

    Args:
        arg1 (str): string name.

    """
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
