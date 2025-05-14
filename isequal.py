a=4
b=4

print(a is b) #exact loc in mem
print( a == b) #value

class Person:
    name = "souju"
    occ = "fd"
    nw = 100
    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person()
print(a.name)
a.name = "tuvi"
print(a.name)
a.info()

#__name__ == "__main__"
