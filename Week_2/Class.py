class pieces:
    def __init__(self, name, position, color, power):
        self.name = name
        self.position = position
        self.color = color
        self.power = power

king = pieces('king', 'ai', 'black', 5)
print(king.name, king.position)