"""
CP1404 Week 8 practical
Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main Program to print labels based on a dictionary of names"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Initialize the main App"""
        super().__init__(**kwargs)
        self.names = {"Jimmy", "Steve", "Michelle", "Tommy"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root


DynamicLabelsApp().run()
