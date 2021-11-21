class Horse:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self,name):
        self.name = name

bond = Rider("James Bond")
thunder = Horse("Thunder","black",bond)
print(thunder.owner.name)