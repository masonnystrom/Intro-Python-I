#__repr__ - goal is to be unambigous(debugging)
# __str__ - goal is to be readable (user output)

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon():
    def __init__(self, lon, lat):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
    def __str__(self):
        return f'Name = {self.name}\nlat = {self.lat}\nlon = {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)
    def __str__(self):
        wpstr = super().__str__()
        diffsize_str = f"\ndifficulty = {self.difficulty} \nsize = {self.size}"
        return wpstr + diffsize_str

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

catacombs = Waypoint("Catacombs", 71.705, -121.01)
print(catacombs)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.02, -121.08)

# Print it--also make this print more nicely
print(geocache)
