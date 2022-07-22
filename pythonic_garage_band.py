# Use Python classes to model a Band made up of different kinds of musicians.
# Start with Guitarist,Bassist, and Drummer.
# Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

# TESTS FOR BAND
# name - string
# members - a list of instances that inherit from the musician base class
# play_solos - method that asks each member musician to play a solo in the order they were added to the band
# __str__
# __repr__
# TESTS FOR MUSICIAN - abstract base class
# Musician (subclass):
# to_list method - returns a list of previously created band instances
# get_instrument - method that returns string
# play_solo - method that returns a string


class Band:
    number_of_members = 0
    members = []

    def __init__(self):
        Band.number_of_members += 1


class Musician:

    def __init__(self, first, instrument):
        self.first = first
        self.instrument = instrument

    def name_and_role(self):
        return f"My name is {self.first} and I play {self.instrument}"


class Guitarist(Musician):
    pass


class Bassist(Musician):
    pass


class Drummer(Musician):
    pass


person = Guitarist('Kyle', 'guitarist')
