"""CP1404 - Week 6 Practical
Guitars

Estimated time to complete: 30 min
Actual time to complete: 42min

"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Define name, year and cost of guitar"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Print a string of guitar information (name, year, cost)"""
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

    def get_age(self):
        """Get guitar and return as an integer"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE



