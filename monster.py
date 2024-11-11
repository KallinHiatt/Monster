class Monster():
    def __init__(self, name, place):
        self.name = name
        self.place = place
        
    def __str__(self):
        return f"This is {self.name} and it lives in {self.place}"

    def attack(self):
        pass


class Mr_Smiley(Monster):
    def __init__(self, name, place):
        super().__init__(name, place)
        
    def attack():
        return f"Mr. Smiley pulls out a ball of string, and smiling, turns the lights off,\nand ties the corpse of your body to the ceiling..."

class WeepingAngels(Monster):
    def __init__(self, name, place):
        super().__init__(name, place)

    def attack():
        return "The Weeping angel, solid as stone, seems innocent and frayed. That is, until you decide to look away from it..."
        
class Snake(Monster):
    def __init__(self, name, place):
        super().__init__(name, place)
        
    def attack():
        return f"The snake slithers into the floor, and doesn't come out until you stop moving.\nWord of advice: Don't stop running..."

class Jeremy(Monster):
    def __init__(self, name, place):
        super().__init__(name, place)
        
    def attack():
        return f"Jeremy is a hugger. He can find you in the darkest of places..."
                
print(Mr_Smiley("Bob", "Sewers"))
print(Mr_Smiley.attack())
print()


print(WeepingAngels("Sandra", "School Buildings"))
print(WeepingAngels.attack())
print()


print(Snake("Wormtounge", "Middle Earth"))
print(Snake.attack())
print()


print(Jeremy("Jeremy", "the shadows"))
print(Jeremy.attack())
