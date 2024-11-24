"""
CP1404 - Programming II
Band class

"""
from musician import Musician


class Band:
    """Band class"""

    def __init__(self, name):
        """Initialise the Band class"""
        self.name = name
        self.musician = []

    def __repr__(self):
        """Print musician and their instrument name"""
        for musician in self.musician:
            return f"{self.musician} plays {musician.instruments}"

    def add(self, musician):
        """Add a musician"""
        self.musician.append(musician)
        return musician

    def play(self):
        """Musician plays instrument"""
        print(f"band {self.name} is playing: ")
        for musicians in self.musician:
            musicians.play()
