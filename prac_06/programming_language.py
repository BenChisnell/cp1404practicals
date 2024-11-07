class ProgrammingLanguage:
    """Display programming language information."""
    def __init__(self,name="",typing="",reflection="",year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string of programming language information."""
        return f"{self.name} , {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language entered is dynamic."""
        return self.typing == "Dynamic"


def second_part_task():

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic:
            print(language.name)

    if __name__ == "__main__":

        second_part_task()