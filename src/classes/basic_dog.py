"""
Dogs contain a list od Dog object instances

"""


# noinspection PyMissingOrEmptyDocstring
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def __str__(self):
        return f"{self.name}, {self.breed}, {self.owner}"


# noinspection PyMissingOrEmptyDocstring
class Dogs:
    def __init__(self):
        self._dog_list = []

    def add_dog(self, dog_obj):
        self._dog_list.append(dog_obj)

    def __len__(self):
        return len(self._dog_list)


if __name__ == '__main__':
    dog = Dog("Stela", "Golden Retriever", "Eric")
    print(dog)
    dogs = Dogs()
    dogs.add_dog(dog)
