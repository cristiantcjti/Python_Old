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

    def __str__(self):
        return f"Name: {self.name} - Year: {self.year} - Likes: {self.likes}."


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration
    
    def __str__(self):
        return f"Name: {self.name} - Year: {self.year} -  Duration: {self.duration} - Likes: {self.likes}."


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__( name, year)
        self.seasons = seasons
    
    def __str__(self):
        return f"Name: {self.name} - Year: {self.year} -  Season: {self.seasons} - Likes: {self.likes}."

class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]
  
    def __len__(self):
        return len(self._programs)

    @property
    def listing(self):
        return self._programs

 




spiderman = Movie("spiderman", 2003, 120)
fast_furious = Movie("fast_furious", 2006, 180)
atlanta = Series("atlanta", 2017, 2)
flash = Series("flash", 2016, 6)

spiderman.give_like()
spiderman.give_like()
spiderman.give_like()

fast_furious.give_like()
fast_furious.give_like()
fast_furious.give_like()
fast_furious.give_like()

atlanta.give_like()

flash.give_like()
flash.give_like()
flash.give_like()

movies_series = [spiderman, fast_furious, atlanta, flash]

weekend_playlist = Playlist("weekend_playlist", movies_series)

print(f'Size of my weekend playlist: {len(weekend_playlist)}')

for program in weekend_playlist:
    print(program)


    
