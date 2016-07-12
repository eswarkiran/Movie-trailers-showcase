class Parent():
    def __init__(self, name, color):
        self.last_name = name
        self.eye_color = color

brad = Parent("mckinsley", "white")
print(brad.eye_color,brad.last_name)
class Child(Parent):
    def __init__(self,name1,color1,toys):
        Parent.__init__(self,name1,color1)
        self.no_toys=toys
chad= Child("ada","black","23")
print(chad.eye_color,chad.no_toys)
print(chad.no_toys)                 

                 
                 
