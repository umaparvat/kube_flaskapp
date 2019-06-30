class Movies:

    def __init__(self, name, year, director):
        self.name = name
        self.year = year
        self.director = director

    def to_obj(self):
        return f"Movies({self.name}, {self.year}, {self.director})"
