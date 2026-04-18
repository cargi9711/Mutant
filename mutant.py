class Mutant:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    def use_power(self):
        return f"{self.name} uses {self.power} at level {self.level}!"

    def __str__(self):
        return f"{self.name} | Power: {self.power} | Level: {self.level}"
