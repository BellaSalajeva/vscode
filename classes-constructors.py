class Point:
    def __init__(self, x, y): #constructor, x and y ued to initialise objects
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)