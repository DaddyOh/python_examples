""" example classes to itterate ove

The advantage of this is that you change how the data is stored and the itterator can hide that
abstraction

"""

class Dogs:



    def __init__(self):
        # so many ways to represent the data
        # taking the easy way not the best
        self.names = []
        self.breeds = []
        self.owners = []

    def add_dog(self, name, breed, owner):
        self.names.append(name)
        self.breeds.append(breed)
        self.owners.append(owner)

    def __iter__(self):
        """ Returns the Iterator object """
        return DogIterator(self)

    def __len__(self):
        return len(self.names)

class DogIterator:
    """
    Class that enables the Dogs to be itterated through a dog at a time

    """
    def __init__(self, dogs_obj):
        # Team object reference
        self._dogs = dogs_obj
        # member variable to keep track of current index
        self._index = 0

    def __next__(self):
        result = None
        """'Returns the next value from dogs object's lists """
        if self._index < (len(self._dogs)):
            # return a tuple but you can return a list or a dict for each dog
            result = (self._dogs.names[self._index],self._dogs.breeds[self._index],
                      self._dogs.owners[self._index])
            self._index += 1
            return result
        # End of Iteration
        raise StopIteration

# TODO add itterator class

if __name__ == "__main__":

    dogs_obj = Dogs()
    dogs_obj.add_dog("Sparky", "Black Lab", "Eric")
    dogs_obj.add_dog("Giant", "Corgi", "Jackie")
    dogs_obj.add_dog("Giant", "Golden Retriever", "Kevin")
    for ct, dog in enumerate(dogs_obj, 1):
        print(f'{ct} {dog}')

