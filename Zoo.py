class Animal:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        self.health=10
        self.happiness=10

    def feed(self):
        self.health+= 10
        self.happiness+= 10
        print(f"{self.name} has been feed")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
         
class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.mane_size="small" if age< 3 else "large"
    def feed(self):
        self.health+= 10
        self.happiness+=10           
        print(f"{self.name} the lion ate meat.")

    def display_info(self):
        super().display_info()
        print(f"Pride: {self.mane_size}")


class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.favorite_fruit ="banana"

    def feed(self):
        self.health+=15
        self.happiness += 5         
        print(f"{self.name} the monkey got {self.favorite_fruit}!")

    def display_info(self):
        super().display_info()
        print(f"Favourite fruit: {self.favorite_fruit}")


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.strength=90   

    def feed(self):
        if self.strength > 70:
            print(f"{self.name} the bear is Very strong")
            return
        self.health += 15          
        self.happiness += 20
        print(f"{self.name} the bear enjoyed")

    def display_info(self):
        super().display_info()
        status = "very strong" if self.strength > 70 else "normal strength"
        print(f"Status: {status}")




class Zoo:
    def __init__(self, zoo_name):
        self.name    = zoo_name
        self.animals = []             

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has joined {self.name}!")

    def feed_all(self):
        print(f" Feeding time at {self.name}!")
        for animal in self.animals:
            animal.feed()

    def print_all_info(self):
        for animal in self.animals:
            animal.display_info()

    def find_animal(self, name):
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal
        return None

    def count(self):
        return len(self.animals)


zoo = Zoo("My Zoo")
zoo.add_animal(Lion("Simba", 5))
zoo.add_animal(Monkey("George", 3))
zoo.add_animal(Bear("Baloo", 7))
zoo.print_all_info()
zoo.feed_all()
print("\nAfter feeding:\n")
zoo.print_all_info()