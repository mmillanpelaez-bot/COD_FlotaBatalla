class Barco:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getwidth(self):
        return self.width
    def getheight(self):
        return self.height

    def setwidth(self, width):
        self.width = width
    def setheight(self, height):
        self.height = height
    def __str__(self):
        return f'{self.width}x{self.height}'