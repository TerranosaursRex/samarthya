class Cars:
    def __init__(self,name,hp,colour):
        self.name=name
        self.colour = colour
        self.hp = hp

    def myfunc(self):
        print(f"hello car name is {self.name} and the colour is {self.colour}\n horsepower is {self.hp}")

    def __str__(self):
            return "Name: "+self.name, "colour: "+(self.colour),  "HP: " +str(self.hp)        
p1 = Cars("aventador",2300,"red")
p1.myfunc()
print(p1)

