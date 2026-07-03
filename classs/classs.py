class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def change_color(self, color):
        self.color = color


classs1 = Cookie(color="Red")
classs2 = Cookie(color="Green")

print("Class 1 Color is :", classs1.get_color())
print("Class 2 Color is :", classs2.get_color())

# Update Color

classs1.change_color(color="Blue")
print("Class 1 Update Color is :", classs1.get_color())


