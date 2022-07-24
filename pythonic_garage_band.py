# ---------------------------- PROBLEM DOMAIN --------------------------------------------------------------------------
# Use classes to model a Band made up of different kinds of musicians.
# Start with Guitarist,Bassist, and Drummer.
# Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

# ---------------------------- BAND REQUIREMENTS -----------------------------------------------------------------------
# Band instance should have a name attribute which is a string.
# Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super)
# class.
# Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were
# added to band.
# Band instance should have appropriate __str__ and __repr__ methods.
# Band should have a class method to_list which returns a list of previously created Band instances

# ---------------------------- MUSICIAN REQUIREMENTS -------------------------------------------------------------------
# Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
# Each kind of Musician instance should have a get_instrument method that returns string.
# Each kind of Musician instance should have a play_solo method that returns string.

# ------------------------------ CLASSES REFERENCE ---------------------------------------------------------------------
# Classes support two types of operations: Attribute references and instantiation.
# ---- Attribute references - obj.name. Attributes are functions and declared variables.
# ---- Class instantiation - x = MyClass(). Uses function notation. This returns a new INSTANCE OBJECT of the class
# (using parameters).

# * CLASS STATE is defined by __init__(). This creates a specific state when the class is called to make a new object.
#   The new object will take on whatever is instantiated in the __init__.
#         class MyClass:
#           def __init__(self, parameter1, parameter2):
#               self.p1 = parameter1
#               self.p2 = parameter2

#           def f(self)
#               return 'hello world'

#         x = MyClass("Kyle", 31)
#         x.p1, x.p2
#         ("Kyle", 31)

# * ATTRIBUTE NAMES : INSTANCE OBJECTS ONLY UNDERSTAND Data Attributes. There's 2 kinds: data attributes and
# methods.
# ** DATA ATTRIBUTES: "instance variables" Don't need to be declared
#                 x.counter = 1
#                 While x.counter < 10
#                   x.counter = x.counter * 2
#                 print(x.counter)
#                 del x.counter
# ** METHODS: methods "belong" to the object. Therefore, it's a method object and not a function object.
#                 x.f() # This passes in 'self' as a parameter automatically.
#                 "hello world"
# * CLASS AND INSTANCE VARIABLES
# ** CLASS VARIABLES - are shared to all instances of the class. 'gamer = True'
# ** INSTANCE VARIABLES - variables that are unique to the instance. 'x.console = "PC"'


# ------------------------------ MUSICIAN CLASS ------------------------------------------------------------------------
class Band:

    def __init__(self):
        self.musician_list = []
        self.instrument_list = []


# ------------------------------- BAND CLASS ---------------------------------------------------------------------------
class Musician(Band):
    # ---- Initiation of state ----
    def __init__(self, name, instrument):
        super().__init__()
        self.name = name
        self.instrument = instrument

        self.musician_list.append(self.name)
        self.instrument_list.append(self.instrument)

    def __str__(self):
        return f'STR: My name is ({self.name}, and I play the {self.instrument})'

    def __repr__(self):
        return f'REPR: My name is {self.name}, and I play the {self.instrument}'

    def add_member(self, member):
        self.list_of_members.append(member)

    def print_list(self):
        return print(self.list_of_members)

    def play_solos(self):
        for i in self.list_of_members:
            return i
    def get_instrument(self):
        return self.instrument


# ---------------------------------- BAND MEMBERS ----------------------------------------------------------------------
class Guitarist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


class Bassist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'


class Drummer(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
