"""

This just shows a few special methods
One that is very useful it to be able to iterate over a class that may have multiple
data elements in the class.

I've used this with data from a database call with thousand's of rows in the class


The advantage of how the iterator works is that you change how the data is stored and yet
the class can hide the data storage abstraction

The iterator can return most anything but you probably want to return a row of results or an object

item # for a single thing returned
# for multiple items returned
tuple
list
dictionary
obj - another class

"""


class Dogs:
    """
    A class that holds information about many instances of a dog
    """

    def __init__(self):
        # list of dogs as class objects
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)

    def __str__(self):
        return f'Example __STR__: There are {self.__len__()} dogs in this object'

    def __repr__(self):
        return f'Example __REPR__: There are {self.__len__()} dogs in this object'

    def __iter__(self):
        """ Returns the Iterator object """
        return DogIterator(self)

    def __len__(self):
        return len(self.dogs)


class DogIterator:
    """
    The magic of iterating over Dogs is created here
    """

    def __init__(self, dogs):
        # Team object reference
        self._dogs = dogs
        # member variable to keep track of current index
        self._index = 0

    def __next__(self):
        result = None
        """'Returns the next value from dogs object's list """
        if self._index < (len(self._dogs)):
            result = self._dogs.dogs[self._index]
            self._index += 1
            return result
        # End of Iteration
        raise StopIteration


class Dog:
    def __init__(self, name, breed, owner):
        # so many ways to represent the data
        # taking the easy way not the best
        self.name = name
        self.breed = breed
        self.owner = owner

    def __hash__(self):
        """
        WARNING
        This is shown for curiosity only.  The docs say do not implement a __hash__() without
        implement __eg__() and also the hash value is salted and so changes each time
        python is run

        :return: A ahs value. See above warning
        """
        return hash((self.name, self.breed, self.owner))

    def __str__(self):
        """
        :return: formatted str for a dog
        """
        return f'{self.name}, {self.breed}, {self.owner}, {self.__hash__()}'

    def __repr__(self):
        """
        :return: same as __str__
        """
        return self.__str__()


if __name__ == '__main__':

    dogs_obj = Dogs()
    dogs_obj.add_dog(Dog("Giant", "Corgi", "Jackie"))
    dogs_obj.add_dog(Dog("Tiny", "Black Lab", "Eric"))
    dogs_obj.add_dog(Dog("Stella", "Golden Retriever", "Kevin"))
    dogs_obj.add_dog(Dog("Stella", "Golden Retriever", "Kevin"))
    dogs_obj.add_dog(Dog("Stella", "Golden Retriever", "David"))

    for ct, dog in enumerate(dogs_obj):
        print(f"{ct} {dog}")

    print(f"len dogs: {len(dogs_obj)}")
    print(dogs_obj)
