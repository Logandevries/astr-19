class FavoriteAnimal:
    def __init__(self, length_of_arms, length_of_legs, number_of_eyes, has_tail, is_furry):
        self.length_of_arms = length_of_arms
        self.length_of_legs = length_of_legs
        self.number_of_eyes = number_of_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe_animal(self):
        print("Length of arms:", self.length_of_arms)
        print("Length of legs:", self.length_of_legs)
        print("Number of eyes:", self.number_of_eyes)
        print("Does it have a tail?", self.has_tail)
        print("Is it furry?", self.is_furry)

# Example usage
animal = FavoriteAnimal(2.5, 3.0, 2, True, True)
animal.describe_animal()