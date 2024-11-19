"""
CP1404 - Week 8 Pracical
Convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.60934


class MilesToKilometersApp(App):
    """Main Program to convert miles to kilometers"""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Calculate distance using user input value and multiply by distance CONSTANT"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KILOMETERS
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Update value in input box using UP / DOWN arrows """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)

    def get_validated_miles(self):
        """Return a valid numeric number"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometersApp().run()
