from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver service taxi class"""
    flagfall = 4.50  # $4.50 flagfall default cost

    def __init__(self, name, fuel, fanciness):
        """Initialize Silver Service Taxi class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string value"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get a fare value"""
        return self.flagfall + super().get_fare()
