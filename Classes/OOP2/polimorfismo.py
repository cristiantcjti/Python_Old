class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()
    
    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1  

    def print_info():
        print(f"Name: {self.name} - Year: {self.year} - Likes: {self.likes}.")


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__("spiderman", 2013)
        self.duration = duration
    
    def print_info(self):
        print(f"Name: {self.name} - Year: {self.year} -  Duration: {self.duration} - Likes: {self.likes}.")


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__("atlanta", 2016)
        self.seasons = seasons
    
    def print_info(self):
        print(f"Name: {self.name} - Year: {self.year} -  Season: {self.seasons} - Likes: {self.likes}.")




spiderman = Movie("spiderman", 2003, 120)
spiderman.give_like()
spiderman.give_like()
spiderman.give_like()

atlanta = Series("atlanta", 2017, 2)
atlanta.give_like()


movies_series = [spiderman, atlanta]

for program in movies_series:
    program.print_info()
