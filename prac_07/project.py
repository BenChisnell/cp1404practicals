"""
CP1404 Practical
Project Management Program
Estimate: 2.5 hours
Actual:
"""
from datetime import datetime


class Project:
    def __init__(self, name="", start_date="", priority=0, estimate=0, completion=0):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Print a string of Project information"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:.2f},completion: {self.completion}%"

    def is_completed(self):
        """Determine if a project is completed."""
        return self.completion == 100
