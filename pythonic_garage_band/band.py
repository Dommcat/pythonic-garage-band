# define musician classes
class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def play_instrument(self):
        return f"plays {self.instrument}"

    def __str__(self):
        return f"My name is {self.name()} and I {self.play_instrument()}"

musician = Musician("I play music")
print(musician)



# define Guitarist (child class) of musician:

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")

    def __str__(self):
        return f"My name is {self.name} and I {self.play_instrument()}"

guitarist = Guitarist("Joan Jett")
print(guitarist)  # "My name is Joan Jett and I play guitar"


# def test_guitarist_str():
#     joan = Guitarist("Joan Jett")
#     actual = str(joan)
#     expected = "My name is Joan Jett and I play guitar"
#     assert actual == expected















if __name__=='__main__':
    John = Musician (John)
    George = Musician (George)
    print (John.print)
    print (George.print)






# Create musicians and pythonic_garage_band
    guitarist = Guitarist('Joan Jet')
    bassist1 = Bassist('Paul')
    drummer1 = Drummer('Ringo')

# Create pythonic_garage_band
    band = Band1('The Beatles')
    band1.hire_musician(guitarist1)
    band1.hire_musician(guitarist2)
    band1.hire_musician(bassist1)
    band1.hire_musician(drummer1)

class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def play_solo(self):
        pass

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'guitar')

    def play_solo(self):
        return 'Guitar solo'

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, 'bass')

    def play_solo(self):
        return 'Bass solo'

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'drums')

    def play_solo(self):
        return 'Drum solo'

 # Define band class
class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def hire_musician(self, musician):
        self.musicians.append(musician)

    def fire_musician(self, musician):
        self.musicians.remove(musician)

    def play_solos(self):
        solos = [musician.play_solo() for musician in self.musicians]
        return solos





musician = Musician("John Doe")
print(musician)  # "My name is John Doe and I play music"

guitarist = Guitarist("Joan Jett")
print(guitarist)  # "My name is Joan Jett and I play guitar"




#



#
# # Play solos
# print(band1.play_solos())


